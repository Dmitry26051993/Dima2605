# Создать бесконечный генератор случайных чисел.
# Использовать в генераторе временную задержку
import random
from time import sleep


def my_gener():
    while True:
        yield random.randint(-5, 5)
        sleep(1)

for i in my_gener():
    print(i)
    if i == 0:
        break