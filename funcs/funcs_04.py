# Реализовать функцию возвращающую матрицу.
# На вход принимает n - размерность матрицы, random_from(по-умолчанию 1), random_to(по-умолчанию(9)).

from random import randint
def main():
    n = int(input("Enter number: "))
    random_from = 1
    random_to = 9
    arr = [[randint(random_from, random_to) for _ in range(n)] for _ in range(n)]
    print(*arr, sep='\n')
main()