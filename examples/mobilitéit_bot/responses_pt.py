hello_intent_text = [
    'olá',
    'oi',
    'ei',
    'começar'
]

bye_intent_text = [
    'tchau',
    'adeus',
    'até logo'
]

help_intent_text = [
    'me ajude',
    'ajuda',
    'o que você pode fazer?'
]

current_location_intent_text = [
    'estou atualmente em CITY', 
    'estou em CITY',
    'me encontro em CITY',
    'estou atualmente na parada STOP', 
    'estou na parada STOP',
    'me encontro na parada STOP',
    'estou em CITY',
    'estou na parada STOP',
    'estou em CITY',
    'estou na parada STOP',
    'estou em CITY',
    'estou na parada STOP'
]

destination_location_intent_text = [
    'quero ir para CITY', 
    'quero seguir para CITY',
    'como chego em CITY',
    'quero ir para a parada STOP', 
    'quero seguir para a parada STOP',
    'como chego na parada STOP'
]

def final_response(bus_name, dep_time):
    return "Você pode pegar o " + bus_name + " que sai às " + dep_time

greeting_text = "Olá! Sou o Mobiliteit-Bot, estou aqui para ajudá-lo a se locomover em Luxemburgo usando o transporte público! Para começar, você pode me dizer de onde deseja partir? (O nome da parada de ônibus ou o nome do local 🚌! Note que atualmente só entendo os nomes em francês 🥺). Peça ajuda a qualquer momento e me diga se quiser mudar de idioma!"

fallback_s0_text = "Não entendi isso 😅 talvez tente pedir ajuda se quiser algumas dicas úteis!"

s1_text = "Você poderia me dizer de onde deseja partir? (O nome da parada de ônibus ou o nome do local 🚌!). Peça ajuda a qualquer momento e me diga se quiser mudar de idioma!"

help_text = "Meu trabalho é ajudar você a encontrar um ônibus ou trem que você possa pegar para viajar para outro local em Luxemburgo 🇱🇺 🚄 🚌! Por enquanto, posso ajudar se você me disser o nome exato de uma parada de ônibus/trem ou se você me disser nomes de cidades. Atualmente, só posso ajudar com caminhos que possuem uma conexão direta, portanto, se uma transferência for necessária, não poderei ajudar 😢"

stop_list_text = "Qual das seguintes paradas de ônibus/trem corresponde à sua? Coloca só o número!\n"

retry_text_1 = "Vamos tentar novamente! De qual parada ou cidade você deseja partir? Leve em consideração que o nome da cidade precisa estar em francês 🤓"

retry_text_2 = "Vamos tentar novamente! Para qual parada ou cidade você deseja viajar? Leve em consideração que o nome da cidade precisa estar em francês 🤓"

def start_location_text(stop):
    return "Certo, seu ponto de partida é " + stop + "!"

def start_location_affirmation_text(chosen_stop):
    return "Sua parada de partida é " + chosen_stop + ", está correto?"

destination_query_text = "Para onde você deseja ir?"

def destination_location_affirmation_text(chosen_stop):
    return "Sua parada de destino é " + chosen_stop + ", está correto?"

def travel_path_text(start, destination):
    return "Certo, você planeja ir de " + start + " para " + destination + ", deixe-me verificar qual ônibus ou trem você pode pegar 😀"

bye_text = "Me avise se eu puder ajudar novamente!"

error_message = "Algo deu errado 😔, talvez o caminho escolhido não tenha uma conexão direta..."

error_language = "Não consegui configurar o idioma para o idioma escolhido, talvez tente perguntar novamente..."

language_choose = "Certo, qual idioma você deseja usar?"
