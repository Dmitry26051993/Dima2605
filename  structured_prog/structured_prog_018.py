# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.
m = int(input("Введите число: "))
n = int(input("Введите число: "))
x = range(m, n)
for i in x:
    for e in range(2, i-1):
        if i % e == 0:
            print(f"{i} : {e}", end = ' ')

m = int(input("Введите число: "))
n = int(input("Введите число: "))
dict = {}
for num in range(m, n + 1):
    dict[num] = []
    for i in range(2, num):
        if num % i == 0:
            dict[num].append(i)
for i in dict.items():
    print(i)