from plates import is_valid

def test_CS50():
    assert is_valid("CS50") == True

def test_CS05():
    assert is_valid("CS05") == False

def test_Pie():
    assert is_valid("PI3.14") == False

def test_time():
    assert is_valid("OUTATIME") == False

def test_integer():
    assert is_valid(5) == False