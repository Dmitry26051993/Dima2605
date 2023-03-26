# Написать функцию по переводу:
# Дюймы в сантиметры, Сантиметры в дюймы,
# Мили в километры, Километры в мили, Фунты в килограммы,
# Килограммы в фунты, Унции в граммы, Граммы в унции, Галлон в литры,
# Литры в галлоны, Пинты в литры, Литры в пинты
# Примечание: функция принимает на вход число, и коэффициент, возвращает конвертированное число.
# Для хранения коэффициент использовать словарь
# Написать программу, со следующим интерфейсом:
# пользователю предоставляется на выбор 12 вариантов перевода(описанных в первой задаче).
# Пользователь вводит цифру от одного до двенадцати. После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат. Использовать функцию из первого задания.
# Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.
inches_to_centimeters = 1
centimeters_to_inches = 2
kilometrs_to_miles = 3
miles_to_kilometrs = 4
exit = 5
def main():
    dict = {"inces": 2.54, "cent": 0.3937, "miles": 0.6214, "kil": 1.61}
    choice = 0
    while choice != exit:
        display_menu()
        choice = int(input("Выберите вариант: "))
        if choice == inches_to_centimeters:
            num = int(input("Введите число: "))
            result = dict["inces"]*num
            print(f"{result} centimeters")
        elif choice == centimeters_to_inches:
            num = int(input("Введите число: "))
            result1 = dict["cent"] * num
            print(f"{result1} inches")
        elif choice == kilometrs_to_miles:
            num = int(input("Введите число: "))
            result2 = dict["miles"] * num
            print(f"{result2} miles")
        elif choice == miles_to_kilometrs:
            num = int(input("Введите число: "))
            result3 = dict["kil"] * num
            print(f"{result3} kilometrs")
        elif choice == exit:
            print("Выходим из программы: ")
        else:
            print("Ошибка: недопустимый выбор.")
def display_menu():
    print("Меню: ")
    print("1. Из дюймов в сантиметры ")
    print("2. Из сантиметров в дюймы ")
    print("3. Из километров в мили ")
    print("4. Из милей в километры")
    print("5. Выход")
main()



