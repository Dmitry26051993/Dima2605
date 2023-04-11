# Реализовать функцию возвращающую матрицу.
# На вход принимает n - размерность матрицы, random_from(по-умолчанию 1), random_to(по-умолчанию(9)).

from random import randint








def create_matrix(n, random_from = 1, random_to = 9):
    matrix = []
    for _ in range(n):
        arr_in = []
        for _ in range(n):
            arr_in.append(randint(random_from, random_to))
            matrix.append(arr_in)
    return matrix
def main():
    print(create_matrix(3))
if __name__ == '__main__':
    main()