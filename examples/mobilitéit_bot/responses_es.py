

hello_intent_text = [
    'hola',
    'hi',
    'hey',
    'start'
]

bye_intent_text = [
    'adiós',
    'hasta luego',
    'nos vemos'
]

help_intent_text = [
    'ayuda',
    'ayúdame',
    '¿qué puedes hacer?',
]

current_location_intent_text = [
    'estoy actualmente en CITY',
    'estoy en CITY',
    'me encuentro en CITY',
    'estoy actualmente en STOP',
    'estoy en STOP',
    'me encuentro en STOP'
]

destination_location_intent_text = [
    'quiero ir a CITY',
    'quiero llegar a CITY',
    'cómo llego a CITY',
    'quiero ir a STOP',
    'quiero llegar a STOP',
    'cómo llego a STOP'
]

def final_response(bus_name, dep_time):
    return "Puedes tomar el " + bus_name + " que sale a las " + dep_time

greeting_text = "¡Hola! Soy el Bot de Mobiliteit y estoy aquí para ayudarte a moverte por Luxemburgo utilizando el transporte público. Para empezar, ¿puedes decirme desde dónde quieres comenzar? (El nombre de la parada de autobús o el nombre del lugar 🚌!, ten en cuenta que actualmente solo entiendo los nombres en francés 🥺). ¡Pide ayuda en cualquier momento y dime si quieres cambiar de idioma!"

fallback_s0_text = "No entendí eso 😅. Tal vez intenta pedir ayuda si deseas algunos consejos útiles."

s1_text = "¿Podrías decirme desde dónde quieres comenzar? (El nombre de la parada de autobús o el nombre del lugar 🚌!, ten en cuenta que actualmente solo entiendo los nombres en francés 🥺). ¡Pide ayuda en cualquier momento y dime si quieres cambiar de idioma!"

help_text = "Mi trabajo consiste en ayudarte a encontrar un autobús o tren que puedas tomar para viajar a otro lugar en Luxemburgo 🇱🇺 🚄 🚌. Por ahora, puedo ayudarte si me dices el nombre exacto de una parada de autobús/tren o si me dices nombres de ciudades. \n Actualmente, solo puedo ayudarte con rutas que tengan una conexión directa, por lo que no podré ayudarte si se requiere un trasbordo 😢."

stop_list_text = "¿Cuál de las siguientes paradas de autobús/tren corresponde a la tuya? ¡Introduce solo el número!\n"

retry_text_1 = "¡Intentémoslo de nuevo! ¿Desde qué parada o ciudad quieres empezar? Ten en cuenta que el nombre de la ciudad debe ser en francés 🤓"
retry_text_2 = "¡Intentémoslo de nuevo! ¿Hacia qué parada o ciudad quieres viajar? Ten en cuenta que el nombre de la ciudad debe ser en francés 🤓"



def start_location_text(stop):
    return "De acuerdo, tu punto de partida es " + stop + "."

def start_location_affirmation_text(chosen_stop):
    return "Tu parada de inicio es " + chosen_stop + ", ¿es correcto?"

destination_query_text = "¿A dónde te gustaría ir?"

def destination_location_affirmation_text(chosen_stop):
    return "Tu destino es " + chosen_stop + ", ¿es correcto?"

def travel_path_text(start, destination):
    return "De acuerdo, planeas ir desde " + start + " hasta " + destination + ". Permíteme verificar qué autobús o tren puedes tomar 😀."

bye_text = "Déjame saber si puedo ayudarte nuevamente."

error_message = "Algo salió mal 😔, tal vez tu ruta elegida no tiene una conexión directa..."

error_language = "No pude establecer el idioma que elegiste, tal vez inténtalo de nuevo..."

language_choose = "Muy bien, ¿qué idioma deseas usar?"