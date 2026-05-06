from fuel import convert, gauge

def test_fraction():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100



def test_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
