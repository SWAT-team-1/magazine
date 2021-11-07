from magazine.magazine_bot import get_response

def test_get_response():
    expected = 'Hello!'
    actual = get_response('hey')
    assert actual == expected

def test_get_response2():
    expected = 'Bye, see you later'
    actual = get_response('bye')
    assert actual == expected

def test_get_response3():
    expected = 'Thanks'
    actual = get_response('thank')
    assert actual == expected