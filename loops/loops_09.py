# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями от 1 до 9.
from random import randint
import random
a = int(input("Введите число: "))
b = int(input("Введите число: "))
matrix = [[random.randrange(1, 10) for y in range(a)] for x in range(b)]
for im in range(b):
    print(matrix[im])
n = int(input("Введите число: "))
arr = []
for i in range(n):
    arr_1 = []
    for j in range(n):
        arr_1.append(randint(1, 9))
    print(arr_1)
    arr.append(arr_1)


