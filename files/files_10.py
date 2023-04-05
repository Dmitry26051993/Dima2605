# Создать csv файл с данными следующей структуры: Имя, Фамилия, Возраст.
# Создать отчетный файл с информацией по количеству людей входящих в ту или иную возрастную группу.
# Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+.
import csv
from csv_utils import create, read

def main():

    fields = ["name", "lastname", "old"]
    rows = [["Alex", "Petrov", 25], ["Sasha", "Morozov", 40], ["Zara", "Red", 12]]
    create("test_3.csv", fields, rows)
    print(read("test_3.csv"))
if __name__ == '__main__':
    main()