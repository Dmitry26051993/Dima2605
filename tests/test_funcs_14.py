def factorial(n: int) -> int:
    result = 1
    for i in range((1 if n % 2 else 2), n + 1, 2):
        result *= i
    return result
def test_1():
    assert factorial(5) == 15
def test_2():
    assert factorial(2) == -14
