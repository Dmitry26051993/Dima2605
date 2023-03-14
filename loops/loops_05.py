# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n) используя цикл while
n = int(input("Введите число: "))
counter = 1
while counter <= n:
    print((counter * (counter + 1) / 2) ** 2)
    counter = counter + 1
sum_ = 0
num = 1
while num <= n:
    sum_ += num ** 3
    num += 1
print(sum_)
sum_1 = [(i ** 3) for i in range(1, n + 1)]
print(sum(sum_1))


