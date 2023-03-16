# Дан произвольный список, содержащий только числа.
# Выведите результат сложения всех чисел больше 10.
from random import randint
my_str = [randint(-20, 20) for i in range(10)]
print(my_str)
my_str2 = []
for i in range(10):
    my_str2.append(randint(-20, 20))
print(my_str2)
result = 0
for i in my_str:
    if i > 10:
        result += i
print(result)