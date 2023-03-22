# Создать функцию, которая принимает на вход неопределенное количество аргументов
# и возвращает их сумму и максимальное из них.
from random import randint
def my_func(*args):
    summ = 0
    for arg in args:
        summ += arg
    return summ
result = my_func(1, 2, 5, 1, 5)
result1 = my_func(max(1, 2, 5, 1, 5))
print(f"end sum = ", result, f"max number = ", result1)
