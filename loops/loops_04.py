# Просуммировать неопределенное количество чисел, вводимых пользователем,
# суммировать до тех пор, пока пользователь не введёт слово «стоп».
# Не учитывать числа кратные 5
i = 0
while True:
    s = input("Введите число: ")
    if s == "стоп":
        break
    else:
        if int(s) % 5 != 0:
            i += int(s)
            print(i)
        else:
            continue
a = 0
while True:
    n = input("Введите число: ")
    if n == "стоп":
        print("The end")
        break
    n = int(n)
    if n % 5 != 0:
        a += int(n)
    print(a)