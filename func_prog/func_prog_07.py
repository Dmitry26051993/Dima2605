# Дан список чисел.
# Найти произведение всех чисел, которые кратны 3.
from functools import reduce
arr = [i for i in range(1, 10)]
print(arr)
new_arr = [i for i in arr if i % 3 == 0]
print(new_arr)
result = reduce(lambda x, y: x * y, new_arr)
print(result)
new_arr2 = filter(lambda x: x % 3 == 0, arr)
result1 = reduce(lambda x, y: x * y, new_arr2)
print(result1)
result2 = reduce(lambda x, y: x * y, filter(lambda x: x % 3 == 0, arr))
print(result2)

