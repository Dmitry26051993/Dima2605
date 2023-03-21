# Дана целочисленная квадратная матрица.
from random import randint
n = int(input("Введите число: "))
m = int(input("Введите число: "))
arr = []
for i in range(n):
    arr_1 = []
    for j in range(m):
        arr_1.append(randint(1, 9))
    print(arr_1)
    arr.append(arr_1)
# Найти в каждой строке наибольший элемент и поменять его местами с элементом главной диагонали.
for i in range(min(n, m)):
    r = arr[i].index(max(arr[i]))
    arr[i][i], arr[i][r] = arr[i][r], arr[i][i]
print(arr)
matrix = [[randint(1, 9)for _ in range(4)] for _ in range(4)]
for arr in matrix:
    print(arr)
for index, arr in enumerate(matrix):
     max_elem = max(arr)
     index_max_elem =arr.index(max_elem)
     arr[index], arr[index_max_elem] = arr[index_max_elem], arr[index]
print("After replase")
for arr in matrix:
    print(arr)