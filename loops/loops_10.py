# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями.
from random import randint
n = int(input("Введите число: "))
arr = []
for i in range(n):
    arr_1 = []
    for j in range(n):
        arr_1.append(randint(1, 9))
    print(arr_1)
    arr.append(arr_1)
# Найти сумму всех элементов матрицы, которые кратны 3.
sum = 0
for arr_i in arr:
    print(arr_i)
    for i in arr_i:
        print(i)
        sum += i

for arr_i in arr:
    print(arr_i)
    for i in arr_i:
        print(i)
        if (i % 3) == 0:
            sum += i
print(sum)