from bank import value

def test_Hello():
    assert value("Hello") == "$0"

def test_How():
    assert value("How you doing") == "$20"

def test_What():
    assert value("What's happening?") == "$100"

def test_integer():
    assert value("20") == "$20"