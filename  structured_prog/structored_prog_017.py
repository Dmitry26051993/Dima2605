# В массиве целых чисел с количеством элементов 19.
import random
arr = []
arr = [random.randint(1, 10) for i in range(19)]
print(arr)
# # Определить максимльное число и заменить им все четные по значению элементы.
print(list(map(lambda x: max(arr) if x % 2 == 0 else x, arr)))
arr = [random.randint(1, 10) for i in range(19)]
print(arr)
for index, number in enumerate(arr):
    if number % 2 == 0:
        arr[index] = max(arr)
print(arr)