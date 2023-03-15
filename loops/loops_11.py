# Дан двумерный массив n × m элементов.
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
count = 0
for arr_i in arr:
    for j in arr_i:
        if j == 7:
            count += 1
print(count)

# Определить, сколько раз встречается число 7 среди элементов массива.