# Создать функцию, которая принимает на вход неопределенное количество именованных аргументов
# и выводит на экран те из них, длина ключа которых четна.
def func(**kwargs):
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
            print(key, value)
func(alex = 1, bella = 2, can = 3)