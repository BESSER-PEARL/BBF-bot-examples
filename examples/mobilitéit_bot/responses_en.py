hello_intent_text = [
    'hello',
    'hi',
    'hey'
]

bye_intent_text = [
    'bye',
    'goodbye',
    'see you'
]

help_intent_text = [
    'help me',
    'help',
    'what can you do?'
]

current_location_intent_text = [
    'i am currently in CITY', 
    'i am in CITY',
    'i find myself in CITY'
    'i am currently in STOP', 
    'i am in STOP',
    'i find myself in STOP',
    'i am at CITY',
    'i am at STOP',
    'im at CITY',
    'im at STOP',
    'i\'m at CITY',
    'i\'m at STOP'
]

destination_location_intent_text = [
    'i want to go to CITY', 
    'i want to aim for CITY',
    'how do i get to CITY'
    'i want to go to STOP', 
    'i want to aim for STOP',
    'how do i get to STOP'
]

def final_response(bus_name, dep_time):
    return "You can take the " + bus_name + " that leaves at " + dep_time

greeting_text = "Hello! I am Mobiliteit-Bot, I am here to help you get around in Luxembourg using public transportation! To start of, could you tell me from where you want to start? (The name of the bus stop or name of the location 🚌!)"

fallback_s0_text = "I didn't understand that 😅 maybe try asking for help if you want some useful tips!"

s1_text = "Could you tell me from where you want to start? (The name of the bus stop or name of the location 🚌!)"

help_text = "My job is to help you find a bus or train that you could take to travel to another location in Luxembourg 🇱🇺 🚄 🚌! As of now, I can help you if you tell me the exact name of a bus/train-stop or if you tell me city-names. \n Currently, I can only help you with paths that possess a direct connection, thus if a transfer is necessary, I will not be able to help 😢"

stop_list_text = "Which of the following bus/train stops correspond to yours? \n"

def start_location_text(stop):
    return "Alright, your starting point is " + stop + "!"

def start_location_affirmation_text(chosen_stop):
    return "Your starting stop is " + chosen_stop + ", is that right?"

destination_query_text = "Where do you want to go?"

def destination_location_affirmation_text(chosen_stop):
    return "Your destination stop is " + chosen_stop + ", is that right?"

def travel_path_text(start, destination):
    return "Alright, you plan to go from " + start + " to " + destination + ", let me check which bus or train you could take 😀"

bye_text = "Let me know if I can help you again!"

error_message = "Something went wrong 😔, maybe your chosen path does not have a direct connection..."

error_language = "I couldn't set the language to your chosen language, maybe try asking again..."

language_choose = "Alright, which language do you want to use?"