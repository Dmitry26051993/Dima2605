# Написать функции по работе с csv файлами в файле csv_utils.py.
# Чтение. Запись. Добавление записи(по позиции, по-умолчанию в конец).
# Удаление записи(по позиции, по-умолчанию последнюю).
# В файле files_08 импортировать функции.
# С помощью функций создать файл с информацией о товарах(Имя товара, цена, количество, комментарий).
# Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.
from csv_utils import create, read, add, delete

def main():
    fields = ["name", "price", "quantity", "comment"]
    rows = [["Ice_cream", 10, 50, "nice"], ["Coffe", 5, 100, "nice"], ["Egg", 2, 500, "nice"]]
    create("test.csv", fields, rows)
    print(read("test.csv"))
    add("test.csv", ["Potato", 3, 10, "well"])
    print(read("test.csv"))
    delete("test.csv", 6)
    print(read("test.csv"))

if __name__ == '__main__':
    main()


