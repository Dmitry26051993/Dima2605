# В массиве целых чисел с количеством элементов 19.
import random
arr = []
i = 1
count = 0
arr = [random.randint(1, 10) for i in range(19)]
print(arr)
# Определить максимльное число и заменить им все четные по значению элементы.
print(list(map(lambda x: max(arr) if x % 2 == 0 else x, arr)))
max_num = max(arr)
for index, number in enumerate(arr):
    if number % 2 == 0:
        arr[index] = max_num
print(arr)

