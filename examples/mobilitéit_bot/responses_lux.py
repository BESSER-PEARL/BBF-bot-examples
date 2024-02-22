hello_intent_text = [
    'moien',
    'salut',
    'hallo',
    'yo',
    'start'
]

bye_intent_text = [
    'addi',
    'äddi',
    'eddi',
    'bye'
    'tschüss',
    'mir gesinn eis'
]

help_intent_text = [
    'hëllef mer',
    'hëllef',
    'wat kanns de maachen?'
]

current_location_intent_text = [
    'ech sinn aktuell zu CITY',
    'ech sinn zu CITY',
    'ech befinn mech zu CITY',
    'ech sinn aktuell op STOP',
    'ech sinn op STOP',
    'ech befinn mech op STOP',
    'ech sinn zu CITY',
    'ech sinn op STOP',
    'ech sinn zu CITY',
    'ech sinn op STOP',
    'ech sinn zu CITY',
    'ech sinn op STOP'
]

destination_location_intent_text = [
    'ech wëll no CITY',
    'ech wëll op CITY goen',
    'wéi kommen ech op CITY',
    'ech wëll op STOP',
    'ech wëll op STOP goen',
    'wéi kommec ech op STOP'
]

def final_response(bus_name, dep_time):
    return "Du kanns den " + bus_name + " deen ëm " + dep_time + " fiert!"

greeting_text = "Moien! Ech sinn den Mobiliteit-Bot, ech sinn hei fir dir am Land mam ëffentlechem Transport ze hëllefen! Fir unzefänken, kinnst du mir soen, wous du grad bass? (De Numm vum Busarret oder de Numm vum Duerf 🚌!, bemierk datt ech momentan nëmmen déi franséisch Nimm versti 🥺). Fro no Hëllef wanns du wëlls an so mir, ob du d'Sprooch wiesselen wëlls!"

fallback_s0_text = "Dat hun ech net verstan 😅. Probeier eventuell fir Hëllef ze Froen, wanns de wëlls!"

s1_text = "Kinnst du mir soen, wous du grad bass? (De Numm vum Busarret oder de Numm vum Duerf 🚌!, bemierk datt ech momentan nëmmen déi franséisch Nimm verstin 🥺). Fro no Hëllef wanns du wëlls an so mir, ob du d'Sprooch wiesselen wëlls!"

help_text = "Meng Aufgab ass et, dir bei der Sich no engem Bus oder Zuch ze ënnerstëtzen, deens du kanns huele fir dech a Lëtzebuerg ze deplacéieren 🇱🇺 🚄 🚌! Am Moment kann ech dir hëllefe wann du mir de genauen Numm vun engem Bus- oder Zucharrêt sees oder wann du mir den Numm vun dengem Duerf sees. Aktuell kann ech dech nëmmen mat Weeër ënnerstëtzen déi eng direkt Verbindung hunn, esou dass ech net kann hëllefen, wann eng kéier Emtseigen néideg ass 😢."

stop_list_text = "Wéieen vun deene folgend Bus-/Zucharrêten kënne mat dengem korrespondéieren? Gëff just d'Nummer an!\n"

retry_text_1 = "Looss eis et nach eng Kéier probéieren! Vun wéi enger Haltestell oder Stad wëlls du ufänken? Huelt w.e.g. zur Kenntnis, dass den Numm vun der Stad op Franséisch muss sinn 🤓"
retry_text_2 = "Looss eis et nach eng Kéier probéieren! Op wéi eng Haltestell oder Stad wëlls du reesen? Huelt w.e.g. zur Kenntnis, dass den Numm vun der Stad op Franséisch muss sinn 🤓"


def start_location_text(stop):
    return "Okay, däi Startpunkt ass " + stop + "!"

def start_location_affirmation_text(chosen_stop):
    return "Dain Ufanks-Arrêt ass " + chosen_stop + ", ass dat richteg?"

destination_query_text = "Wou wëlls de higoen?"

def destination_location_affirmation_text(chosen_stop):
    return "Dain Ziel-Arrêt ass " + chosen_stop + ", ass dat richteg?"

def travel_path_text(start, destination):
    return "Okay, dain Plang ass et, vun " + start + " op " + destination + " ze goen. Looss mech iwwerpréiwen, weieen Bus oder de Zuch du huelen kanns😀."

bye_text = "Sooh mer Bescheed, wann du nach Hëllef brauchs!"

error_message = "Eppes ass schief gaangen 😔. Et kéint sinn, dass deng gewielte Streck keng direkt Verbindung huet..."

error_language = "Ech konnt d'Sprooch net op deng gewielte Sprooch setzen, probeier et vläicht nach eng Kéier..."

language_choose = "Alles gudd, wéieng Sprooch wëlls de benotzen?"
