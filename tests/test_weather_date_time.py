from magazine.weather import get_weather
from magazine.magazine_bot import get_response
import datetime
x = datetime.datetime.now()

def test_get_weather():
    expected = 'Amman'
    actual = get_weather('amman')[19:24]
    assert actual == expected

def test_get_date():
    day = x.strftime("%A")
    expected = f'Today is {day}'
    response = get_response('date')
    actual = response.split(',')[0]
    assert actual == expected

def test_get_time():
    expected = x.strftime("%X")
    actual = get_response('time')[12:20]
    assert actual == expected
