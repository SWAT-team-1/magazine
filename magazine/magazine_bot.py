import re

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
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
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo','hola','welcome'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Thanks', ['thank', 'thanks','that\'s helpful'], single_response=True)
    response('My name is Magazine', ['name','what is your name', 'whats your name'])
    response('Bye, see you later', ['bye', 'goodbye','see you later', 'nice chatting to you, bye', 'till next time'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return 'Please give me more info' if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input, user_name=None):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


if __name__ =='__main__':
    print("Start messaging with the Magazine bot (type quit to stop)!")
    user_name = input('Bot: ' + 'Enter Your Name: ')
    while True:
        print(user_name.capitalize() +': ', end="")
        user_input = input()
        if user_input.lower() in ['quit', 'q', 'exit','bye', 'goodbye','see you later', 'nice chatting to you, bye', 'till next time']:
            print('Bot: Bye, see you later')
            quit()
        else:
            print(  'Bot: ' + get_response(user_input, user_name))