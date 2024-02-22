import logging
import pandas as pd
import requests
import responses_lux
import responses_en
import responses_cat
import responses_de
import responses_fr
import responses_es
import responses_pt
import re
import operator

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from besser.bot.nlp.intent_classifier.intent_classifier_prediction import IntentClassifierPrediction
from besser.bot.core.bot import Bot
from besser.bot.core.session import Session
from besser.bot.library.entity.base_entities import number_entity


# Configure the logging module
logging.basicConfig(level=logging.INFO, format='{levelname} - {asctime}: {message}', style='{')
responses = responses_en
# Create the bot
bot = Bot('mobiliteit_bot')
# Load bot properties stored in a dedicated file
bot.load_properties('config.ini')
# Define the platform your chatbot will use
websocket_platform = bot.use_websocket_platform(use_ui=True)
telegram_platform = bot.use_telegram_platform()
# STATES
# Init state
s0 = bot.new_state('s0', initial=True)
# Init state after 1st walkthrough
s1 = bot.new_state('s1')
# Global help state in case of problems
help_state = bot.new_state('help_state')
# State to process the user's current location
current_location_state = bot.new_state('current_location_state')

# Fallback state to figure the user's current location
current_location_fallback_state = bot.new_state('current_location_fallback_state')
# Retry state 1
current_location_retry_state = bot.new_state('retry_state_1')
# Retry state 2
destination_location_retry_state = bot.new_state('retry_state_2')
# State to process the user's destiny location
destination_location_state = bot.new_state('destination_location_state')
# Fallback state to figure the user's destiny location
destination_location_fallback_state = bot.new_state('destination_location_fallback_state')
# State to change language of bot
language_state = bot.new_state('language_state')
# State to finalize language change
chose_language_state = bot.new_state('chosen_language_state')
# Final state to inform user of path
final_state = bot.new_state('final_state')

# Additional functions or pre-processing

# Download any gtfs file from https://data.public.lu/en/datasets/horaires-et-arrets-des-transport-publics-gtfs/ 
# Extract the stops.txt file and convert it to stops.csv
data = pd.read_csv("stops.csv")
stops = dict()
# use base entity numbers here
for n, stop in enumerate(data["stop_name"]): 
    stops[stop] = []

cities = dict()
for stop in data["stop_name"]:
    city = stop.split(",")[0]
    if city not in cities:
        cities[city] = []
    if "-" in city:
        split_city = city.split("-")
        cities[split_city[0]] = []


# Get available trips from startId to destId
def get_trip_info(startId: str, destId: str, responses):
    payload = {}
    payload["accessId"] = "YOUR MOBILITEIT API TOKEN HERE"
    payload["id"] = startId
    payload["direction"] = destId
    payload["format"] = "json"
    payload["maxJourney"] = 1
    r = requests.get('https://cdt.hafas.de/opendata/apiserver/departureBoard', params=payload)
    message = ""
    response = r.json()
    if ("Departure" in response):
        departure = response["Departure"][0]
        bus_name = departure["name"]
        dep_time = departure["time"]
        if ("rtTime" in departure):
            dep_time = departure["rtTime"] 
        message = responses.final_response(bus_name, dep_time) 
    return message

        
# INTENTS
hello_intent = bot.new_intent('hello_intent', responses_fr.hello_intent_text + responses_en.hello_intent_text + responses_de.hello_intent_text + responses_lux.hello_intent_text + responses_cat.hello_intent_text + responses_es.hello_intent_text + responses_pt.hello_intent_text)
bye_intent = bot.new_intent('bye_intent', responses_en.bye_intent_text + responses_fr.bye_intent_text + responses_de.bye_intent_text + responses_lux.bye_intent_text + responses_cat.bye_intent_text + responses_es.bye_intent_text+ responses_pt.bye_intent_text)
help_intent = bot.new_intent('help_intent', responses_en.help_intent_text + responses_fr.help_intent_text + responses_de.help_intent_text + responses_lux.help_intent_text + responses_cat.help_intent_text + responses_es.help_intent_text + responses_pt.help_intent_text)
language_intent = bot.new_intent('language_intent', [
    'language',
    'change language',
    'change the language',
    # Luxembourgish
    'Sprooch',
    'Sprooch änneren',
    #'Ech wëll d Sprooch änneren',
    #'Kënnen mir d Sprooch änneren',
    'd Sprooch änneren',
    # German
    'Sprache',
    'Sprache ändern',
    #'Ich möchte die Sprache ändern',
    #'Können wir die Sprache ändern',
    'die Sprache ändern',
    'die Sprache ändern',
    # French
    'langue',
    'changer de langue',
    #'je veux changer de langue',
    'pouvons-nous changer de langue',
    # Spanish
    'idioma',
    'cambiar de idioma',
    'quiero cambiar el idioma',
    '¿podemos cambiar el idioma',
    # Catalan
    'idioma',
    'canviar d idioma',
    'vull canviar l idioma',
    'podem canviar l idioma',
    # other
    'francais',
    'deutsch',
    'catalan',
    'letzebuergesch',
    'english',
    'spanish',
    'espanol',
    'french',
    'german',
    'luxembourgish',
    'francais?',
    'deutsch?',
    'catalan?',
    'letzebuergesch?',
    'letz',
    'letz?',
    'english?',
    'spanish?',
    'espanol?',
    'french?',
    'german?',
    'luxembourgish?',
    'mudar idioma',
    'mudar o idioma',
    'portugues',
    'portuguese',
    'portugues?',
    'português',
    'português?'
])
no_intent = bot.new_intent('no_intent',['No', 'Not at all', 'Absolutely not', 'No way', 'No', 'De cap manera', 'De cap de les maneres', 'De cap manera', 'No', 'De ninguna manera', 'Ni hablar', 'En absoluto', 'Nein', 'nö', 'Keineswegs', 'Absolut nicht', 'Non', 'Pas du tout', 'Absolument pas', 'En aucun cas', 'Nee', 'Op kee Fall', 'Absolut net', 'Sécher net','Não','De jeito nenhum','Absolutamente não','De forma alguma','Não'])
stop_city_intent = bot.new_intent('stop_city_intent',[
    'STOP',
    'CITY',
    'to CITY'
])
number_intent = bot.new_intent('number_intent',[
    'NUM'
])
stop_entity = bot.new_entity('stop_entity', entries=stops)
city_entity = bot.new_entity('city_entity', entries=cities)
language_entity = bot.new_entity('language_entity', entries={
    "Francais": ["Francais", "French", "francais", "french", "fr"],
    "German": ["german", "deutsch", "Deutsch"],
    "Spanish": ["Espanol", "Spanish", "Español", "espanol", "spanish", "español"],
    "Catalan": ["Catalan", "catalan", "català", "catala"],
    "Luxembourgish": ["Luxembourgish", "Letzebuergesch", "Lëtzebuergesch", "Luxembourgeois"],
    "English": ["english", "anglais", "england"]
})
current_location_intent = bot.new_intent('current_location_intent', responses_en.current_location_intent_text + responses_fr.current_location_intent_text + responses_de.current_location_intent_text + responses_lux.current_location_intent_text + responses_cat.current_location_intent_text + responses_es.current_location_intent_text + responses_pt.current_location_intent_text)
destination_location_intent = bot.new_intent('destination_location_intent', responses_en.destination_location_intent_text + responses_fr.destination_location_intent_text + responses_de.destination_location_intent_text + responses_lux.destination_location_intent_text + responses_cat.destination_location_intent_text + responses_es.destination_location_intent_text + responses_pt.destination_location_intent_text)
language_state.set_global(language_intent)
help_state.set_global(help_intent)

#language_intent.parameter('lang1', 'LANG', language_entity)
current_location_intent.parameter('stop1', 'STOP', stop_entity)
destination_location_intent.parameter('stop1', 'STOP', stop_entity)
stop_city_intent.parameter('stop1', 'STOP', stop_entity)
stop_city_intent.parameter('city1', 'CITY', city_entity)
current_location_intent.parameter('city1', 'CITY', city_entity)
destination_location_intent.parameter('city1', 'CITY', city_entity)
number_intent.parameter('num1', 'NUM', number_entity)

# Adding a custom handler for the Telegram Application: command /help


# STATES BODIES' DEFINITION + TRANSITIONS

def s0_body(session: Session):
    session.set("wildcard", "0")
    # would be amazing to access gps data
    # expect either city, bus stop or train station
    if not session.get("responses"):
        session.set("responses", responses_en)
    session.reply(session.get("responses").greeting_text)


s0.set_body(s0_body)

def fallback_body_s0(session: Session):
    session.reply(session.get("responses").fallback_s0_text)


s0.set_fallback_body(fallback_body_s0)

s0.when_intent_matched_go_to(current_location_intent, current_location_state)
s0.when_intent_matched_go_to(stop_city_intent, current_location_state)
s0.when_intent_matched_go_to(hello_intent, s0)

def s1_body(session: Session):
    session.reply(session.get("responses").s1_text)
    
    
s1.set_body(s1_body)

s1.when_intent_matched_go_to(current_location_intent, current_location_state)
s1.when_intent_matched_go_to(stop_city_intent, current_location_state)


def current_location_body(session: Session):
    predicted_intent: IntentClassifierPrediction = session.predicted_intent
    if(predicted_intent.matched_parameters and predicted_intent.get_parameter('city1') is not None and predicted_intent.get_parameter('city1').value is not None):
        city = predicted_intent.get_parameter('city1').value
        session.set("city",city)
        stops = data[data["stop_name"].str.match("(?i)" + city)]
        response = session.get("responses").stop_list_text
        index = 1
        session.set("stops", stops["stop_name"])
        for stop in stops["stop_name"]:
            response = response + str(index) +". "+ stop + " \n"
            index += 1
        session.set("wildcard", "1")
        session.reply(response)  
    elif (predicted_intent.matched_parameters and predicted_intent.get_parameter('stop1') is not None and predicted_intent.get_parameter('stop1').value != None):
        stop = predicted_intent.get_parameter('stop1').value 
        session.set("start", stop)
        session.reply(session.get("responses").start_location_text(stop))
        session.reply(session.get("responses").destination_query_text)
    else:
        if (session.get("start") != None):
            session.reply(session.get("responses").destination_query_text)


current_location_state.set_body(current_location_body)
current_location_state.when_intent_matched_go_to(number_intent, current_location_fallback_state)
current_location_state.when_variable_matches_operation_go_to(dest=current_location_fallback_state, operation=operator.eq, target="1", var_name="wildcard")
current_location_state.when_intent_matched_go_to(stop_city_intent, destination_location_state)
current_location_state.when_intent_matched_go_to(destination_location_intent, destination_location_state)
current_location_state.when_no_intent_matched_go_to(current_location_state)

def current_location_fallback_body(session: Session):
    print("State: " + session.current_state.name + " 125")
    msg = session._message
    predicted_intent: IntentClassifierPrediction = session.predicted_intent
    try:
        if (predicted_intent.matched_parameters):
            msg = predicted_intent.get_parameter('num1').value
        index = int(msg)
        chosen_stop = session.get("stops").iloc[index-1]
        print("chose stop")
        print(chosen_stop)
        session.set("start", chosen_stop)
        session.reply(session.get("responses").start_location_affirmation_text(chosen_stop))
        session.set("wildcard", 0)
    except: 
        chosen_stop = session.get("stops").iloc[0]
        session.set("start", chosen_stop)
        session.reply(session.get("responses").start_location_affirmation_text(chosen_stop))
        session.set("wildcard", 0)


current_location_fallback_state.set_body(current_location_fallback_body)
# Go back to current location state regardless of what user writes
current_location_fallback_state.when_intent_matched_go_to(intent=no_intent, dest=current_location_retry_state)
current_location_fallback_state.when_no_intent_matched_go_to(current_location_state)

def retry_body_1(session: Session):
    session.delete("start")
    session.reply(session.get("responses").retry_text_1)

current_location_retry_state.set_body(retry_body_1)
current_location_retry_state.when_intent_matched_go_to(current_location_intent, current_location_state)
current_location_retry_state.when_intent_matched_go_to(stop_city_intent, current_location_state)

def destination_location_body(session: Session):
    dest_stop = None
    predicted_intent: IntentClassifierPrediction = session.predicted_intent
    if (session.get("dest") is None):
        if (predicted_intent.matched_parameters and predicted_intent.get_parameter('stop1') is not None and predicted_intent.get_parameter('stop1').value is not None):
            dest_stop = predicted_intent.get_parameter('stop1').value
            session.set("dest",dest_stop)
        elif (predicted_intent.matched_parameters and predicted_intent.get_parameter('city1') is not None and predicted_intent.get_parameter('city1').value is not None):
            city = predicted_intent.get_parameter('city1').value
            session.set("city", city)
            stops = data[data["stop_name"].str.match("(?i)" + city)]
            response = session.get("responses").stop_list_text
            index = 1
            session.set("stops", stops["stop_name"])
            if (stops["stop_name"].size == 100):
                session.set("dest", stops["stop_name"].iloc[0])
                # this is problematic, as I have to input something for the next state to take place
            #  session.current_state.go_to(current_location_state)
            else: 
                for stop in stops["stop_name"]:
                    response = response + str(index) + ". " + stop + " \n"
                    index += 1
                session.set("wildcard", "1")
                session.reply(response)

    else:
        dest_stop = session.get("dest")
    if dest_stop is not None:
        session.reply(session.get("responses").travel_path_text(session.get("start"), dest_stop))
        start = data[data["stop_name"].str.match("^" + re.escape(session.get("start")) + "$")]
        destination = data[data["stop_name"].str.match("^" + re.escape(dest_stop) + "$")]
        response = get_trip_info(start["stop_id"], destination["stop_id"], session.get("responses"))
        if response != "":
            session.reply(response)    
            session.reply(session.get("responses").bye_text)
        else:
            session.reply(session.get("responses").error_message)        
        session.delete("dest")
        session.delete("start")
        

destination_location_state.set_body(destination_location_body)


destination_location_state.when_intent_matched_go_to(number_intent, destination_location_fallback_state)
destination_location_state.when_variable_matches_operation_go_to(dest=destination_location_fallback_state, operation=operator.eq, target="1", var_name="wildcard")
destination_location_state.when_intent_matched_go_to(stop_city_intent, current_location_state)
destination_location_state.when_intent_matched_go_to(hello_intent, s0)
destination_location_state.when_no_intent_matched_go_to(s1)

def destination_fallback_body(session: Session):
    msg = session.message
    stops = data[data["stop_name"].str.match("(?i)" + msg)]
    response = session.get("responses").stop_list_text
    index = 1
    session.set("stops",stops["stop_name"])
    for stop in stops["stop_name"]:
        response = response + str(index) + ". " + stop + " \n"
        index += 1
    session.reply(response)

current_location_state.set_fallback_body(destination_fallback_body) 
destination_location_state.set_fallback_body(destination_fallback_body)


def destination_location_fallback_body(session: Session):
    msg = session._message
    predicted_intent: IntentClassifierPrediction = session.predicted_intent
    try:
        if (predicted_intent.matched_parameters):
            msg = predicted_intent.get_parameter('num1').value
        index = int(msg)

        chosen_stop = session.get("stops").iloc[index-1]
        session.set("dest", chosen_stop)
        print("chosen stop is " + chosen_stop)
        session.reply(session.get("responses").destination_location_affirmation_text(chosen_stop))
        session.set("wildcard", "0")
    except:
        chosen_stop = session.get("stops").iloc[0]
        session.set("dest", chosen_stop)
        session.reply(session.get("responses").destination_location_affirmation_text(chosen_stop))       
        session.set("wildcard", "0")
        

destination_location_fallback_state.set_body(destination_location_fallback_body)
# Go back to destination location state regardless of input
destination_location_fallback_state.when_intent_matched_go_to(intent=no_intent, dest=destination_location_retry_state)
destination_location_fallback_state.when_no_intent_matched_go_to(destination_location_state)

def retry_body_2(session: Session):
    session.delete("dest")
    session.reply(session.get("responses").retry_text_2)

destination_location_retry_state.set_body(retry_body_2)
destination_location_retry_state.when_intent_matched_go_to(destination_location_intent, destination_location_state)
destination_location_retry_state.when_intent_matched_go_to(stop_city_intent, destination_location_state)


# Global states

def language_body(session: Session):
    session.reply(session.get("responses").language_choose)
    session.reply("1. English \n2. Deutsch\n3. Francais\n4. Español\n5. Catalá\n6. Lëtzebuergesch\n7. Português")


language_state.set_body(language_body)
language_state.when_intent_matched_go_to(number_intent, chose_language_state)


def chose_language_body(session: Session):
    global responses
    msg = session.message
    predicted_intent: IntentClassifierPrediction = session.predicted_intent
    if (predicted_intent.matched_parameters):
        msg = predicted_intent.get_parameter('num1').value
    index = int(msg)
    match index:
        case 1:
            session.set("responses", responses_en)
            session.reply("Alright, language set to English 🏴󠁧󠁢󠁥󠁮󠁧󠁿!")
        case 2:
            session.set("responses", responses_de)
            session.reply("Okay, Sprache auf Deutsch eingestellt 🇩🇪!")
        case 3:
            session.set("responses", responses_fr)
            session.reply("D'accord, langue définie sur le français 🇫🇷!")
        case 4:
            session.set("responses", responses_es)
            session.reply("Vale, idioma establecido en español 🇪🇸!")
        case 5:
            session.set("responses", responses_cat)
            session.reply("D'acord, idioma establert en català 🇦🇩!")
        case 6:
            session.set("responses", responses_lux)
            session.reply("Okay, d'Sprooch gouf op Lëtzebuergesch agestallt 🇱🇺!")
        case 7:
            session.set("responses", responses_pt)
            session.reply("Ok, o idioma foi configurado para Português 🇵🇹!")
        case _:
            session.reply(responses.error_language)


chose_language_state.set_body(chose_language_body)


def help_body(session: Session):
    session.reply(session.get("responses").help_text)


help_state.set_body(help_body)


# current_location_state.when_intent_matched_go_to(destination_location_intent, destination_location_state)



# RUN APPLICATION
if __name__ == '__main__':
    bot.run()

"""
Additional ideas: 
Add possiblity to request more departures
Add possibility to ask for bops stops in my area
Try to implement connecting bus stops
"""