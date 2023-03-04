#Запросить у пользователя два целых числа.
# Вывести строку вида “2 плюс 3 равно 5”
# Примечание: после ввода переменных преобразовать переменные к типу int
# >> first_number = int(first_number)
first_number = int(input('Введите число x: '))
secend_number = int(input('Введите чмсло y: '))
three_number = first_number + secend_number
print(first_number, "плюс", secend_number, "ровно", three_number)