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

def summ_and_max(*args):
    return sum(args), max(args)
def main():
    result = summ_and_max(1, 2, 3, 4, 4, 5, 6)
    print(result, type(result))
    summ, max_elem = summ_and_max(1, 2, 3, 4, 4, 5, 6)
    print(f"summ = {summ}, max_elem = {max_elem}")
if __name__ == '__main__':
    main()