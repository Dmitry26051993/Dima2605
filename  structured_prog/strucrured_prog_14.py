# Дано число. Найти сумму и произведение его цифр.
n = int(input("Введите число: "))
suma = 0
mult = 1
while n > 0:
    digit = n % 10
    suma = suma + digit
    mult = mult * digit
    n = n // 10
print("Сумма:", suma)
print("Произведение:", mult)