# Создать функцию, которая принимает на вход неопределенное количество именованных аргументов
# и выводит на экран те из них, длина ключа которых четна.
def print_from_dict(**kwargs):
    res_dict = {}
    print(kwargs, type(kwargs))
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
            print(key, value)
            res_dict[key] = value
    return res_dict
def main():
    print_from_dict(a=1, bb=2, ccc=3)
if __name__ == '__main__':
    main()