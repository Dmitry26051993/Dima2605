# Использовать результаты files_08. Все функции описываются в csv_utils.py.
# Проверка работы функции осуществляется в files_09.py.
# 1. Создать функцию подсчета полной суммы всех товаров.
# 2. Создать функцию поиска самого дорогого товара.
# 3. Создать функцию самого дешевого товара.
# 4. Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)
from csv_utils import summa, max_price, min_price, minus, create, read
def main():
    fields = ["name", "price", "quantity", "comment"]
    rows = [["Ice_cream", 10, 50, "nice"], ["Coffe", 5, 100, "nice"], ["Egg", 2, 500, "nice"]]
    create("test1.csv", fields, rows)
    print(read("test1.csv"))
    summa("test1.csv")
    print(read("test1.csv"))


if __name__ == '__main__':
    main()

