# Даны катеты прямоугольного треугольника.
# Найти его гипотенузу и площадь.
from math import sqrt
x = int(input('Введите катет x: '))
y = int(input('Введите катет y: '))
c = sqrt((x ** 2) + (y ** 2))
a = (x * y) / 2
print(c)
print(a)