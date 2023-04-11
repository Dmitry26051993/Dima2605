from funcs.funcs_09 import counter_numbers_in_list
def test_counter_numbers_in_list():
    res = counter_numbers_in_list([1, 2, 3, 4, 4, 5, 5, 5, 5, 5])
    assert res == {1: 1, 2: 1, 4: 2, 5: 5}
