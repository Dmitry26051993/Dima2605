def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def test_1():
    assert factorial(5) == 120
def test_2():
    assert factorial(4) == 24
