from funcs.funcs_07 import print_from_dict
def test_print_from_dict():
   res = print_from_dict(a=1, bb=2, ccc=3)
   assert res == {}
def test_print_from_dict1():
    res = print_from_dict(a=1, ccc=3)
    assert res == {}