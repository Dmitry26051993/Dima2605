# Создать csv файл с данными о ежедневной погоде. Структура:  Дата, Место, Градусы, Скорость ветра.
# Найти среднюю погоду(скорость ветра и градусы) для Минск за последние 7 дней.
from csv_utils import create, read
def main():
    fields = ["date", "local", "temperature", "speed"]
    rows = [
        [15, "Minsk", 4, 15],
        [16, "Minsk", 6, 21],
        [17, "Minsk", -2, 25],
        [18, "Minsk", 7, 9],
        [19, "Minsk", 1, 5],
        [20, "Minsk", 0, 7],
        [21, "Minsk", 3, 18],
    ]
    create("test_4.csv", fields, rows)
    print(read("test_4.csv"))
if __name__ == '__main__':
    main()