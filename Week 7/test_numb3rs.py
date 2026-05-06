from numb3rs import validate

def test_validate():
    assert validate("127.0.0.1") == True

def test_validate_leading_zero():
    assert validate("001.2.003.4") == False
    