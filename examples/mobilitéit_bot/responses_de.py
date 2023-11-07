hello_intent_text = [
    'hallo',
    'hi',
    'hey'
]

bye_intent_text = [
    'tschüss',
    'auf Wiedersehen',
    'bis bald'
]

help_intent_text = [
    'hilf mir',
    'hilfe',
    'was kannst du tun?'
]

current_location_intent_text = [
    'ich bin derzeit in CITY',
    'ich befinde mich in CITY',
    'ich befinde mich in CITY',
    'ich bin derzeit an STOP',
    'ich bin an STOP',
    'ich befinde mich an STOP',
    'ich bin in CITY',
    'ich bin an STOP',
    'ich bin in CITY',
    'ich bin an STOP',
    'ich bin in CITY',
    'ich bin an STOP'
]

destination_location_intent_text = [
    'ich möchte nach CITY',
    'ich möchte nach CITY',
    'wie komme ich nach CITY',
    'ich möchte nach STOP',
    'ich möchte nach STOP',
    'wie komme ich nach STOP'
]

def final_response(bus_name, dep_time):
    return "Du kannst den " + bus_name + " nehmen, der um " + dep_time + " abfährt."

greeting_text = "Hallo! Ich bin Mobiliteit-Bot und ich bin hier, um dir zu helfen, dich in Luxemburg mit öffentlichen Verkehrsmitteln fortzubewegen! Um zu beginnen, könntest du mir bitte sagen, von wo aus du starten möchtest? (Name der Bushaltestelle oder Name des Ortes 🚌!)"

fallback_s0_text = "Das habe ich nicht verstanden 😅. Versuche doch, nach Hilfe zu fragen, wenn du nützliche Tipps möchtest!"

s1_text = "Könntest du mir bitte sagen, von wo aus du starten möchtest? (Name der Bushaltestelle oder Name des Ortes 🚌!)"

help_text = "Meine Aufgabe ist es, dir zu helfen, einen Bus oder Zug zu finden, den du nutzen kannst, um an einen anderen Ort in Luxemburg zu reisen 🇱🇺 🚄 🚌! Im Moment kann ich dir helfen, wenn du mir den genauen Namen einer Bus- oder Zug-Haltestelle nennst oder wenn du mir Städtenamen nennst. Aktuell kann ich dir nur bei Direktverbindungen helfen, daher werde ich nicht in der Lage sein zu helfen, wenn ein Umstieg erforderlich ist 😢."

stop_list_text = "Welche der folgenden Bus-/Zug-Haltestellen entsprechen deiner? \n"

def start_location_text(stop):
    return "Alles klar, dein Startpunkt ist " + stop + "!"

def start_location_affirmation_text(chosen_stop):
    return "Deine Start-Haltestelle ist " + chosen_stop + ", ist das korrekt?"

destination_query_text = "Wo möchtest du hin?"

def destination_location_affirmation_text(chosen_stop):
    return "Deine Ziel-Haltestelle ist " + chosen_stop + ", ist das korrekt?"

def travel_path_text(start, destination):
    return "Alles klar, du planst von " + start + " nach " + destination + " zu fahren. Lass mich überprüfen, welchen Bus oder Zug du nehmen könntest 😀."

bye_text = "Lass mich wissen, wenn ich dir wieder helfen kann!"

error_message = "Etwas ist schiefgelaufen 😔. Möglicherweise hat deine gewählte Route keine Direktverbindung..."

error_language = "Ich konnte die Sprache nicht auf deine gewählte Sprache setzen. Versuche es vielleicht noch einmal..."

language_choose = "Okay, welche Sprache möchtest du verwenden?"