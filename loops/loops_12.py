# Дана целочисленная матрица А[n,m].
from random import randint
n = int(input("Введите число: "))
m = int(input("Введите число: "))
arr = []
for i in range(n):
    arr_1 = []
    for j in range(m):
        arr_1.append(randint(-9, 9))
    print(arr_1)
    arr.append(arr_1)
print(arr)
# Посчитать количество элементов матрицы,
sum = 0
count = 0
for arr_i in arr:
    for i in arr_i:
        sum += i
        count += 1
avg = sum / count
print(sum)
# превосходящих среднее арифметическое значение элементов матрицы и сумма индексов которых четна.
for i, arr in enumerate(arr):
    for r, number in enumerate(arr_i):
        if number > avg and ((i + r) % 2) == 0:
            count += 1
print(count)
