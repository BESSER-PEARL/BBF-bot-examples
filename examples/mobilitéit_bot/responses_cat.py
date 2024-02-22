hello_intent_text = [
    'hola',
    'bon dia',
    'ei',
    'start'
]

bye_intent_text = [
    'adeu',
    'fins aviat',
    'fins la propera'
]

help_intent_text = [
    'ajuda’m',
    'ajuda',
    'què pots fer?'
]

current_location_intent_text = [
    'estic actualment a CITY',
    'estic a CITY',
    'em trobo a CITY',
    'estic actualment a STOP',
    'estic a STOP',
    'em trobo a STOP',
    'estic a CITY',
    'estic a STOP',
    'estic a CITY',
    'estic a STOP',
    'estic a CITY',
    'estic a STOP'
]

destination_location_intent_text = [
    'vull anar a CITY',
    'vull dirigir-me a CITY',
    'com puc arribar a CITY',
    'vull anar a STOP',
    'vull dirigir-me a STOP',
    'com puc arribar a STOP'
]

def final_response(bus_name, dep_time):
    return "Pots agafar l'autobús " + bus_name + " que surt a les " + dep_time

greeting_text = "Hola! Sóc el Bot Mobiliteit i estic aquí per ajudar-te a desplaçar-te pel Lluxemburg utilitzant el transport públic! Per començar, podríes dir-me d'on vols començar? (El nom de l'estació d'autobús o el nom del lloc 🚌!, tingues en compte que actualment només entenc els noms en francès 🥺). Demana ajuda en qualsevol moment i digue'm si vols canviar d'idioma!"

fallback_s0_text = "No he entès això 😅. Potser intenta demanar ajuda si vols alguns consells útils!"

s1_text = "Podries dir-me d'on vols començar? (El nom de l'estació d'autobús o el nom del lloc 🚌!, tingues en compte que actualment només entenc els noms en francès 🥺) Demana ajuda en qualsevol moment i digue'm si vols canviar d'idioma!"

help_text = "La meva feina és ajudar-te a trobar un autobús o tren que puguis agafar per anar a un altre lloc de Luxemburg 🇱🇺 🚄 🚌! De moment, només puc ajudar-te si em dius el nom exacte d'una parada d'autobús o tren, o si em dius noms de ciutats. Actualment, només puc ajudar-te amb rutes que tinguin una connexió directa, així que si es requereix un transbordament, no podré ajudar 😢."

stop_list_text = "Quines de les següents parades d'autobús/tren corresponen a la teva? Introdueix només el número!\n"

retry_text_1 = "Tornem-ho a provar! Des de quina parada o ciutat vols començar? Tingues en compte que el nom de la ciutat ha de ser en francès 🤓"
retry_text_2 = "Tornem-ho a provar! Cap a quina parada o ciutat vols viatjar? Tingues en compte que el nom de la ciutat ha de ser en francès 🤓"



def start_location_text(stop):
    return "D'acord, el teu punt de partida és " + stop + "!"

def start_location_affirmation_text(chosen_stop):
    return "La teva parada d'inici és " + chosen_stop + ", és correcte?"

destination_query_text = "On vols anar?"

def destination_location_affirmation_text(chosen_stop):
    return "La teva parada de destinació és " + chosen_stop + ", és correcte?"

def travel_path_text(start, destination):
    return "D'acord, tens la intenció d'anar de " + start + " a " + destination + ". Deixa'm comprovar quin autobús o tren pots agafar 😀."

bye_text = "Fes-me saber si puc ajudar-te de nou!"

error_message = "Alguna cosa ha anat malament 😔. Potser la ruta que has triat no té una connexió directa..."

error_language = "No he pogut establir l'idioma que has triat, potser prova de demanar-ho de nou..."

language_choose = "D'acord, quina llengua vols utilitzar?"