# Написать программу для работы с матрицами:
from random import randint
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
def craete_matrix(n: int) -> list:
    matrix = [[randint(1, 9)for _ in range(n)]for _ in range(n)]
    return matrix

def print_matrix(matrix: list) -> None:
    for arr in matrix:
        print(arr)

def matrix_sum(matrix: list) -> int:
    result = 0
    for arr in matrix:
        result += sum(arr)
    return result

def max_element(matrix):
    return max([max(arr) for arr in matrix])

def min_element(matrix):
    return min([min(arr) for arr in matrix])

def main():
    matrix = craete_matrix(3)
    print_matrix(matrix)
    summa = matrix_sum(matrix)
    print(summa)
    max_elem = max_element(matrix)
    print(f"max element = {max_elem}")
    min_elem = min_element(matrix)
    print(f"min element = {min_elem}")

if __name__ == '__main__':
   main()

