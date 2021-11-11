from magazine.magazine_bot import get_response, message_probability

def test_get_response():
    expected = ["Hello!","Hello, thanks for asking", "Good to see you again", "Hi there, how can I help?"]
    actual = get_response('hey')
    if actual in expected:
        expected = actual
    else:
        expected =None
    assert actual == expected

def test_get_response2():
    expected = ["Bye", "See you later", "Goodbye", "Nice chatting to you, bye", "Till next time"]
    actual = get_response('bye')
    if actual in expected:
        expected = actual
    else:
        expected = None
    assert actual == expected

def test_get_response3():
    expected = ["Happy to help!", "Any time!", "My pleasure"]
    actual = get_response('thank')
    if actual in expected:
        expected = actual
    else:
        expected = None
    assert actual == expected

def test_get_response_when_quit():
    expected = ["Bye", "See you later", "Goodbye", "Nice chatting to you, bye", "Till next time"]
    actual = get_response('q')
    if actual in expected:
        expected = actual
    else:
        expected = None
    assert actual == expected

def test_message_probability():
    expected = 0
    actual = message_probability('goal',['year','football'])
    assert actual == expected
