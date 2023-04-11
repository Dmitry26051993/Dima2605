# Создать функцию, которая принимает на вход неопределенное количество аргументов
# и возвращает их сумму и максимальное из них.
from random import randint

def summ_and_max(*args):
    return sum(args), max(args)
def main():
    result = summ_and_max(1, 2, 3, 4, 4, 5, 6)
    print(result, type(result))
    summ, max_elem = summ_and_max(1, 2, 3, 4, 4, 5, 6)
    print(f"summ = {summ}, max_elem = {max_elem}")
if __name__ == '__main__':
    main()