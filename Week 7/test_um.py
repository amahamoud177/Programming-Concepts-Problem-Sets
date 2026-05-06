from um import count

def test_count():
    assert count("um") == 1

def test_capital():
    assert count("Um") == 1

def test_sentence():
    assert count("Um, thanks for the album") == 1