def my_func(*args):
    summ = 0
    for arg in args:
        summ += arg
    return summ

def test_my_func():
    result = my_func(1, 2, 5, 1, 5)
    assert result == 25

def test_my_func_1():
    result1 = my_func(max(1, 2, 5, 1, 5))
    assert result1 == 6
