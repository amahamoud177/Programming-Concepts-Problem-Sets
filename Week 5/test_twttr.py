from twttr import shorten

def test_twter():
    assert shorten("Twitter") == "Twttr"

def test_question():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_cs50():
    assert shorten("CS50") == "CS50"

def test_hello():
    assert shorten("Hello, World!") == "Hello, Wrld!"
