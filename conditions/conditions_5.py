# Ввести число, проверить на то, что было введено именно число.
a = input("Введите число: ")
# Возвести его в куб и вывести результат на экран.
if a.isdecimal():
    a = int(a)
    result = a ** 3
    print(result)
else:
    print("This is not a namber")