# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n) используя цикл while
n = int(input("Введите число: "))
counter = 1
while counter <= n:
    print((counter * (counter + 1) / 2) ** 2)
    counter = counter + 1

