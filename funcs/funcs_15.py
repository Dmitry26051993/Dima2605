# Даны три слова.
# Выяснить, является ли хоть одно из них палиндромом ("перевертышем"),
# т.е. таким, которое читается одинаково слева направо и справа налево.
# (Определить функцию, позволяющую распознавать слова палиндромы.)
def polindrom(my_str):
    my_str1 = my_str[::-1]
    if my_str == my_str1:
        print("Палиндром")
    else:
        print("Не палиндром")
def main():
    polindrom("lol")
    polindrom("Apple")
    polindrom("mamam")
if __name__ == '__main__':
    main()




