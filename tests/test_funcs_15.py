from funcs.funcs_15 import polindrom
def test_pol():
    res = polindrom("asa")
    assert res == True

def test_pol1():
    res = polindrom("aaq")
    assert res == False