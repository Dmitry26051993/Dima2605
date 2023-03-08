# Ввести строку с клавиатуры
my_str = input("Введите предложение: ")
len_my_str = len(my_str)
# Если длина строки больше 5 - вывести значение на экран
# Если длина строки меньше 5 - вывести строку “Need more!”
# Если длина строки равна 5 - вывести строку “len str == 5”
if len_my_str > 5:
    print(my_str)
elif len_my_str < 5:
    print("Need more!")
elif len_my_str == 5:
    print("len str == 5")