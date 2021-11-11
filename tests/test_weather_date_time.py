import emoji
from magazine.weather import get_weather, emoji_dic
from magazine.magazine_bot import get_response
import datetime
x = datetime.datetime.now()

def test_get_weather():
    expected = 'Amman'
    actual = get_weather('amman')[19:24]
    assert actual == expected

def test_get_weather2():
    expected = 'Dubai'
    actual = get_weather('dubai')[19:24]
    assert actual == expected

def test_get_date():
    day = x.strftime("%A")
    expected = f'Today is {day}'
    response = get_response('date')
    actual = response.split(',')[0]
    assert actual == expected

def test_get_time():
    expected = x.strftime("%X")[:5]
    actual = get_response('time')[12:17]
    assert actual == expected

def test_variables():
    assert emoji_dic['clear sky'] == ':sun:'

def test_variables2():
    assert emoji_dic['mist'] == ':fog:'