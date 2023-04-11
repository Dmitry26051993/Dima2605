# Дан массив целых чисел A.
# Найти суммы положительных и отрицательных элементов массива,
# используя функцию определения суммы.
from random import randint

def my_func():
    arr = [randint(-5, 10) for _ in range(10)]
    print(arr)
    sum1 = 0
    sum2 = 0
    for i in arr:
        if i > 0:
            sum1 += i
        else:
            sum2 += i
    return sum1, sum2
def main():
    sum1, sum2 = my_func()
    print(f"Сумма положительных чисел: {sum1}, сумма отрицательных чисел: {sum2}")
if __name__ == '__main__':
    main()
