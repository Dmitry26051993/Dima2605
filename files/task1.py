# Гипотеза Коллатца утверждает, что любое натуральное число превратится в единицу, если к нему достаточно много раз последовательно применить преобразование f. Вот
# пример – сколько раз нужно применить f, чтобы превратить в единицу первые несколько
# натуральных чисел:
# 1: 0 раз (это и так единица);
# 2: 1 раз (2 → 1);
# 3: 7 раз (3 → 10 → 5 → 16 → 8 → 4 → 2 → 1);
# 4: 2 раза (4 → 2 → 1);
# 5: 5 раз (5 → 16 → 8 → 4 → 2 → 1).
# Напишите функцию collatz с одним аргументом n. Функция должна возвращать
# 2-элементный кортеж:
# – первый элемент – число k (1 ≤ k < n) такое, что у него самая длинная траектория
# среди всех чисел в диапазоне [1, n);
def col(n):
    arr = [n]
    if n < 1:
        return []
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        arr.append(n)
    for i in arr:
        print(i, end=' ')

col(int(input("Введите число: ")))

def colltz(n):
    my_dict = {}
    for i in range(2, n + 1):
        item = i
        my_list = []
        while item != 1:
            if item % 2:
                item = 3 * item + 1
                my_list.append(item)
            else:
                item = item // 2
                my_list.append(item)
        my_dict[len(my_list)] = str(i)

    max_length = max(my_dict.keys())
    return int(my_dict[max_length]), max_length
def main():
    print(colltz(3))
if __name__ == '__main__':
   main()
