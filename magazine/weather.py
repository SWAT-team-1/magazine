import requests
import colorama 
colorama.init()
from colorama import Fore, Style
import emoji

api_key = "082f8afa8423e4fa6ac472b17510d896"
emoji_dic = {'clear sky':':sun:','overcast clouds':':thought_balloon:' ,'few clouds':':sun_behind_cloud:','scattered clouds':':thought_balloon:','Boken clouds':':thought_balloon:','Shower rain':':cloud with rain:' ,'rain':':sun_behind_rain_cloud:','thunderstorm':':cloud_with_lightning:','snow':':snowflake:','mist':':fog:'}

def get_weather(city_name):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city_name, api_key)

    response = requests.get(api_url)
    response_dict = response.json()

    weather_temp = response_dict['main']['temp']
    weather_description = response_dict['weather'][0]['description']
    emoji_char = emoji.emojize(emoji_dic[weather_description])
    temp_char = emoji.emojize(':thermometer:')
    weather = "The temperature in {} is {}{} Celsius and the weather is {} {}".format(city_name.capitalize(),weather_temp, temp_char,weather_description,emoji_char)
    
    if response.status_code == 200:
        return weather
    else:
        response = 'Soory! Faild to get the weather'
        return response

if __name__ == '__main__':
        
    print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)

    print(Fore.BLUE + 'User: ' + Style.RESET_ALL,end="")
    user_input = input()
    if user_input.lower() in ['quit','q','exit','e','stop']:
        quit()
    else:
        weather = get_weather(user_input)
        print(weather)