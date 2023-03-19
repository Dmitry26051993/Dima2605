# В массиве целых чисел с количеством элементов 19.
import random
arr = []
i = 1
count = 0
arr = [random.randint(-10, 10) for i in range(1, 20)]
print(arr)
# Определить максимльное число и заменить им все четные по значению элементы.
max_num = max(arr)
print(max_num)