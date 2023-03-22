# Написать программу для нахождения факториала.
# Факториал натурального числа n определяется как произведение всех натуральных чисел от 1 до n включительно

def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)

print(factorial(int(input('Введите число: '))))