# Создать lambda функцию, которая принимает
# на вход неопределенное количество именованных аргументов
# и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}
arr = (lambda **kwargs: {key * 2: value for key, value in kwargs.items()})(abs=2, war=3)
print(arr)
