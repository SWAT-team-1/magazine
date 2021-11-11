from magazine.translate_feature import *

def test_translate():
    expected ='Bonjour'
    actual=get_translater("hello","fr")
    assert actual == expected

def test_translate2():
    expected = 'أهلا بك'
    actual=get_translater("welcome","ar")
    assert actual == expected

def test_translate3():
    expected = 'Gracias'
    actual=get_translater("Thank you","es")
    assert actual == expected

def test_variables():
    assert languages['ar'] == 'arabic'