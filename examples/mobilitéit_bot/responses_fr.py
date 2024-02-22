hello_intent_text = [
    'salut',
    'bonjour',
    'coucou',
    'start'
]

bye_intent_text = [
    'au revoir',
    'à bientôt',
    'à la prochaine'
]

help_intent_text = [
    'aide-moi',
    'aide',
    'que peux-tu faire?'
]

current_location_intent_text = [
    'je suis actuellement à CITY',
    'je suis à CITY',
    'je me trouve à CITY',
    'je suis actuellement à STOP',
    'je suis à STOP',
    'je me trouve à STOP',
    'je suis à CITY',
    'je suis à STOP',
    'je suis à CITY',
    'je suis à STOP',
    'je suis à CITY',
    'je suis à STOP'
]

destination_location_intent_text = [
    'je veux aller à CITY',
    'je veux me rendre à CITY',
    'comment puis-je arriver à CITY',
    'je veux aller à STOP',
    'je veux me rendre à STOP',
    'comment puis-je arriver à STOP'
]

def final_response(bus_name, dep_time):
    return "Tu peux prendre le bus " + bus_name + " qui part à " + dep_time

greeting_text = "Salut ! Je suis le Bot Mobiliteit, et je suis là pour t'aider à te déplacer au Luxembourg en utilisant les transports publics ! Pour commencer, peux-tu me dire d'où tu veux partir ? (Le nom de l'arrêt de bus ou le nom de l'endroit 🚌 ! note que je comprends actuellement uniquement les noms en français 🥺). N'hésite pas à demander de l'aide à tout moment et dis-moi si tu veux changer de langue!"

fallback_s0_text = "Je n'ai pas compris ça 😅. Peut-être essaie de demander de l'aide si tu veux des conseils utiles !"

s1_text = "Peux-tu me dire d'où tu veux partir ? (Le nom de l'arrêt de bus ou le nom de l'endroit 🚌 ! note que je comprends actuellement uniquement les noms en français 🥺). N'hésite pas à demander de l'aide à tout moment et dis-moi si tu veux changer de langue!"

help_text = "Mon travail consiste à t'aider à trouver un bus ou un train que tu pourrais prendre pour te rendre dans un autre endroit au Luxembourg 🇱🇺 🚄 🚌 ! Pour l'instant, je peux t'aider si tu me donnes le nom exact d'un arrêt de bus ou de train, ou si tu me donnes des noms de villes. Actuellement, je ne peux t'aider qu'avec des trajets en connexion directe, donc si un transfert est nécessaire, je ne pourrai pas t'aider 😢."

stop_list_text = "Lesquels parmi les arrêts de bus/train suivants correspondent au tien ? Entre juste le numéro!\n"

retry_text_1 = "Essayons à nouveau ! De quel arrêt ou quelle ville veux tu partir ? Garde à l'esprit que le nom de la ville doit être en français 🤓"
retry_text_2 = "Essayons à nouveau ! Vers quel arrêt ou quelle ville veux tu voyager ? Garde à l'esprit que le nom de la ville doit être en français 🤓"


def start_location_text(stop):
    return "D'accord, ton point de départ est " + stop + " !"

def start_location_affirmation_text(chosen_stop):
    return "Ton arrêt de départ est " + chosen_stop + ", c'est bien ça ?"

destination_query_text = "Où veux-tu aller ?"

def destination_location_affirmation_text(chosen_stop):
    return "Ton arrêt de destination est " + chosen_stop + ", c'est bien ça ?"

def travel_path_text(start, destination):
    return "D'accord, tu prévois d'aller de " + start + " à " + destination + ". Laisse-moi vérifier quel bus ou train tu pourrais prendre 😀."

bye_text = "Fais-moi savoir si je peux t'aider à nouveau !"

error_message = "Quelque chose s'est mal passé 😔. Peut-être que ton itinéraire choisi n'a pas de connexion directe..."

error_language = "Je n'ai pas pu définir la langue que tu as choisie. Peut-être essaye de demander à nouveau..."

language_choose = "D'accord, quelle langue souhaitez-vous utiliser ?"