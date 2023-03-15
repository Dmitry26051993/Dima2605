# Написать игру. Пользователь должен угадать число.
# Сперва вводится диапазон угадывания. После колличество попыток.
# В случае правильного ответа - выводить You are the winner.
# В случае неправильного давать игроку подсказку(больше или меньше искомое число).
# Если за указанное количество попыток число не угадано - выводить: You are the loser и правильное число.
import random

numbers_range = input("Введите диапазон чисел в формате - : ")
attempts = int(input("Введите число попыток: "))
begin, end = map(int, numbers_range.split("-"))
hidden_number = random.randint(begin, end)

for _ in range(attempts):
    number = int(input("Угадай число: "))
    if number == hidden_number:
        print("You are the winner")
        break
    elif number < hidden_number:
        print("Число должно быть больше!")
    elif number > hidden_number:
        print("Число должно быть меньше!")

else:
    print("You are the loser".format(hidden_number))
