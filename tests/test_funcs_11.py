from funcs.funcs_11 import is_power_n
def test_is_power_n1():
    res = is_power_n(9, 3)
    assert res == True
def test_is_power_n2():
    res = is_power_n(2, 3)
    assert res == False
