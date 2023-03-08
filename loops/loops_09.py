# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями от 1 до 9.
import random
a = int(input("Введите число: "))
b = int(input("Введите число: "))
matrix = [[random.randrange(0, 10) for y in range(a)] for x in range(b)]
for im in range(b):
    print(matrix[im])