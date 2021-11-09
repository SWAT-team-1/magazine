from magazine.translate_feature import *
def test_translate():
    expected ='Bonjour'
    actual=get_translater("hello","fr")
    assert actual == expected
    