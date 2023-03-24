# Написать программу для нахождения факториала.
# Факториал натурального числа n определяется как произведение всех натуральных чисел от 1 до n включительно

def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)

print(factorial(int(input('Введите число: '))))

def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    print(factorial(5))
if __name__ == '__main__':
    main()
