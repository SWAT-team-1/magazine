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
    response = f'''I offer information about Date {emoji.emojize(':calendar:')}

                               Time {emoji.emojize(':ten_o’clock:')}
    
                               Weather {emoji.emojize(':sunrise_over_mountains:')}
    
                               Soccer match schedule {emoji.emojize(':soccer_ball:')}
    
                               Movies {emoji.emojize(':clapper_board:')}
    
                               Stock market {emoji.emojize(':chart_increasing:')}
    
                               Tranlation {emoji.emojize(':speech_balloon:')}'''
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

if __name__ == '__main__':
    pass