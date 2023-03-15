# Просуммировать неопределенное количество чисел, вводимых пользователем.
a = 0
while True:
    s = input('Введите числа: ')
    if s.isdigit():
        a += int(s)
    elif s == "стоп":
        break
    else:
        break
print(a)
b = 0
while True:
    l = input("Введите числа: ")
    if l == "stop":
        break
    b += int(l)
    print(b)
# Суммировать до тех пор, пока пользователь не введёт слово «стоп».