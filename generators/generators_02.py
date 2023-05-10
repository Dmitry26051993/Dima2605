# Создать бесконечный генератор случайных чисел.
# Генератор должен принимать диапазон случайных чисел и смещение
# Пример: a = 1, b = 10, diff = 10
# 1-10
# 11-20
# …
# N + 10 - M + 10
import random
def my_gener(a, b, diff):
    while True:
        a += diff
        b += diff
        yield random.randint(a, b)


my_gen = my_gener(-1, 10, 10)
for i in range(5):
    print(next(my_gen))



