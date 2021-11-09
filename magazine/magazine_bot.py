import re
import magazine.long_resp as resp
import colorama 
colorama.init()
from colorama import Fore, Style
from magazine.weather import get_weather
from magazine.goal import get_all_data1
from magazine.stock_market_bot import get_daily_stock_exchange, get_stock_table_report
from magazine.movies_bot import all_movie_function
from magazine.translate_feature import get_translater

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    """
    Counts how many words are present in each predefined message
    then, calculates the percent of recognised words in a user message
    """
    
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    """
    check the massage that comes from the user
    then simplifies response creation / adds it to the dict
    """
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response(resp.greeting(), ['hello', 'hi', 'hey', 'sup', 'heyo','hola','welcome'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response(resp.thanks(), ['thank', 'thanks','helpful'], single_response=True)
    response('My name is Magazine', ['name','what is your name', 'whats your name'])
    response(resp.options(),['help','provide','offer','do','can do'])
    response(resp.good(),['good','great','fine','okay', 'ok','well'])
    response(resp.bad(),['bad', 'sad'])
    response(resp.goodbye(), ['quit', 'q', 'exit','bye','goodbye','see you later', 'nice chatting to you, bye', 'till next time'])
    response(resp.r_advice, ['give', 'advice'], required_words=['advice'])
    response(resp.r_eating, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response('In which Country or city', ['weather', 'temperature', 'what is the temperature', 'what is the weather'])
    response(resp.date(),['today','date'])
    response(resp.time(),['time'])
    response('soccer match schedule',['soccer','football','match','sport','sports'])
    response('stock market',['stock','market','ase'])
    response('movies',['movies','movie','cinema'])
    response('Write your word or sentence',['translate','translater','translation'], required_words=['translate'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return resp.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input, user_name=None):
    """
    get the response according to the user input 
    by bass the user input to check_all_messages funcrion after simplifies

    arguments: user_input, user_name
    output: response for the highest prop response depending on the user input
    """
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    if response == 'In which Country or city':
        print(Fore.GREEN + 'Bot: ' + response + Style.RESET_ALL)
        print(Fore.BLUE + user_name.capitalize() +': ' + Style.RESET_ALL, end="")
        user_input = input()
        response = get_weather(user_input)

    if response == 'soccer match schedule':
        url = 'https://www.goal.com/en/live-scores'
        response = get_all_data1(url, user_name)
    
    if response == 'stock market':
        print(Fore.RED + '''
****************************************************************************
******                                                                ******
******              Welcome to the STOCK MARKET section               ******
******                                                                ******
****************************************************************************'''+ Style.RESET_ALL)
        url = 'https://www.ase.com.jo/en/bulletins/daily/new'
        get_daily_stock_exchange(get_stock_table_report(url), user_name)
        response = 'Do you want anything else?'
    
    if response == 'movies':
        all_movie_function(user_name)
        response = 'Do you want anything else?'
    
    if response == 'Write your word or sentence':
        response = get_translater(user_name=user_name)
    return response


if __name__ == '__main__':
    print(Fore.YELLOW + "Start messaging with the Magazine bot (type quit to stop)!" + Style.RESET_ALL)
    user_name = input(Fore.GREEN + 'Bot: ' + 'Enter Your Name: ' + Style.RESET_ALL)
    while True:
        print(Fore.BLUE + user_name.capitalize() +': ' + Style.RESET_ALL, end="")
        user_input = input()
        if user_input.lower() in ['quit', 'q', 'exit','bye', 'goodbye','see you later', 'nice chatting to you, bye', 'till next time']:
            print(Fore.GREEN + 'Bot: ' + resp.goodbye() + Style.RESET_ALL)
            quit()
        else:
            print(Fore.GREEN + 'Bot: ' + get_response(user_input, user_name) + Style.RESET_ALL)