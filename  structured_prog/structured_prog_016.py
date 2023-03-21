# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают
# (каждое следующее число больше предыдущего).
import random
arr = [random.randint(1, 9) for el in range(15)]
print(arr)
result = 0
count = 0
for j in range(len(arr)-2):
    if arr[j+2] > arr[j+1] > arr[j]:
        count += 1
    elif count >= 1 and arr[j+1] > arr[j+2]:
        result += 1
        count = 0
if arr[-1] > arr[-2] > arr[-3]:
    result += 1
print(result)