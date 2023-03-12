# Введите число.
my_number = int(input("Введите число: "))
# Если это число делиться на 1000 без остатка, то выведите на экран "millennium"
if my_number % 1000 == 0:
    print("Millennium")
else:
    print("Not millennium")
