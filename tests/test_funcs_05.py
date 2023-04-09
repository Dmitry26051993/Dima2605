def sum_args(*args):
    print(args, type(args))
    result = 0
    for index, number in enumerate(args):
        result = index * number
    return result
def test_sum_args():
    assert sum_args(1, 2, 5) == 9

def test_sum_args1():
    assert sum_args(1, 2, 5) == 10