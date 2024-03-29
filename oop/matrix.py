#  Создать класс Matrix. Атрибуты - data(содержит саму матрицу - список списков), n, m.
#  Определить конструктор(с параметрами(передача размерности:
#  n, m и диапазона случайных чисел: a, b),
#  по-умолчанию(матрица 5 на 5 где все элементы равны нулю),
#  переопределить магический метод __str__ для красивого вывода.
# Описать функции, которые принимают на вход объект класса Matrix.
# Функции позволяют искать максимальный элемент матрицы, минимальный, сумму всех элементов.
# Создать в файле main.py матрицу. Воспользоваться всеми описанными функциями и методами
from random import randint


class Matrix:
    def __init__(self, data=None, n=5, m=5, start_random=0, finish_random=0):
        if data:
            self.__n = data.__n
            self.__m = data.__m
            self.__data = data.__data
        else:
            self.__n = n
            self.__m = m
            self.__data = [[randint(start_random, finish_random)
                            for _ in range(m)] for _ in range(n)]

    def __str__(self):
        return f'{self.__data}'

    @property
    def data(self):
        return self.__data

    def max_element(self):
        element = max([max(row) for row in self.__data])
        return element

    def min_element(self):
        element = min([min(row) for row in self.__data])
        return element

    def sum_matrix(self):
        sum_matrix = sum([sum(row) for row in self.__data])
        return sum_matrix


def max_element(matrix: Matrix):
    element = max([max(row) for row in matrix.data])
    return element


def min_element(matrix: Matrix):
    element = min([min(row) for row in matrix.data])
    return element


def sum_matrix(matrix: Matrix):
    sum_matrix = sum([sum(row) for row in matrix.data])
    return sum_matrix


def main():
    matrix_1 = Matrix(start_random=1, finish_random=10)
    print(matrix_1, matrix_1.sum_matrix(),
          matrix_1.max_element(), matrix_1.min_element())
    print(sum_matrix(matrix_1), max_element(matrix_1), min_element(matrix_1))
    matrix_2 = Matrix(matrix_1)
    print(matrix_2)


if __name__ == '__main__':
    main()