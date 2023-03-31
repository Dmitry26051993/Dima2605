# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных - удалять все четные элементы из списка.
from random import randint
def my_decorator(func):
    def wrapper(arr):
        print(arr)
        new_arr = [i for i in arr if i % 2]
        return func(new_arr)

    return wrapper


@my_decorator
def real_func(arr):
    return arr

arr = [randint(1, 10) for i in range(10)]
print(real_func(arr))