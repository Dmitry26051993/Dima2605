from funcs.funcs_06 import summ_and_max
def test_my_func():
    res = summ_and_max(1, 2, 3)
    assert res == (1, 4)