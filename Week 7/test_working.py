from working import convert


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_convert_minutes():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"

def test_convert_colom():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"