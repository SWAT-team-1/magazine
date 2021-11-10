import random
import datetime
import emoji

"""
This file is to get the responses for the bot when 
the user chatting with the bot depending on the user inputs
"""
r_eating = "I don't like eating anything because I'm a bot obviously!"
r_advice = "If I were you, I will sleep!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "Sorry, can't understand you", 
                "Please give me more info", 
                "Not sure I understand",
                "What does that mean?"][
        random.randrange(5)]
    return response

def greeting():
    response = ["Hello!","Hello, thanks for asking", "Good to see you again", "Hi there, how can I help?"][
        random.randrange(4)]
    return response

def goodbye():
    response = ["Bye", "See you later", "Goodbye", "Nice chatting to you, bye", "Till next time"][
        random.randrange(5)]
    return response

def thanks():
    response = ["Happy to help!", "Any time!", "My pleasure"][random.randrange(3)]
    return response

def options():
    response = f'''I offer information about date {emoji.emojize(':calendar:')}
                                         
                               time {emoji.emojize(':ten_o’clock:')}

                               weather {emoji.emojize(':thought_balloon:')}
                                         
                               soccer match schedule {emoji.emojize(':soccer_ball:')}
                                         
                               movies {emoji.emojize(':clapper_board:')}
                                         
                               stock market {emoji.emojize(':chart_increasing:')}
                                         
                               translation {emoji.emojize(':speech_balloon:')}'''
    return response

def good():
    response = ['great!', 'Happy to hear that', 'All time'][random.randrange(3)]
    return response

def bad():
    response = 'Sad to hear that'
    return response

def date():
    date = datetime.datetime.now()
    now_date = date.strftime('%x')
    today = date.strftime('%A')
    emoji_chr = emoji.emojize(':calendar:')
    response = f'Today is {today}, {now_date} {emoji_chr}'
    return response

def time():

    time = datetime.datetime.now()
    now_time = time.strftime('%X')
    emoji_chr = emoji.emojize(':ten_o’clock:')
    response = f'The time is {now_time} {emoji_chr}'
    return response
def joke():
    response = ["I ate a clock yesterday, it was very time-consuming.",
    "I can’t believe I got fired from the calendar factory. All I did was take a day off!",
    "I went to see the doctor about my short-term memory problems — the first thing he did was make me pay in advance",
    "You have two parts of the brain, “left” and “right”. On the left side, there’s nothing right and on the right side, there’s nothing left."
    ][random.randrange(4)]
    return response
if __name__ == '__main__':
    pass