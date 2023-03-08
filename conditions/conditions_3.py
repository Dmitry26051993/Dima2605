# Запросить у пользователя возраст.
a = int(input("Введите Ваш возраст: "))
# Если возраст меньше 0 - вывести Wrong input, если меньше 18 - вывести Cola, иначе - вывести Beer
if a < 0:
    print("Wrong input")
elif a < 18:
    print("Cola")
else:
    print("Beer")