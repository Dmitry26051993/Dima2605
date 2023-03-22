# Написать программу для работы с матрицами:
from random import randint
import array as arr
def my_func(d, r):
    print("В результате мы выполнили", d)
    print("Результат", r)

# Создание
arr = []
my_func("Создали: ", arr)
# Вывод
arr = [[randint(1, 9) for _ in range(4)] for _ in range(4)]
my_func("Вывели: ", arr)
# Сумма всех элементов
total = 0
for row in arr:
    for num in row:
        total += num
my_func("Сумма всех элементов", total)
# Нахождение максимального элемента
max_num = max(arr)
my_func("Нашли максимальный элемент", max_num)
# Нахождение минимального элемента.
min_num = min(arr)
my_func("Нашли минимальный элемент", min_num)