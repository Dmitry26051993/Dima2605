# Написать программу, в которой вводятся два операнда Х и Y и знак операции sign (+, –, /, *).
while True:
   sign = input("Внесите знак: ")
   if sign == "0":
       print("The end")
       break
   elif sign not in ("+", '-', "*", "/"):
       print("Wrong sing try again")
       continue
   x = int(input("Введите х: "))
   y = int(input("Введите y: "))
   if sign == "+":
       print(f'x + y = {x + y}')
   elif sign == '-':
        print(f"x - y = {x - y}")
   elif sign == "/":
       if y == 0:
           print("Нельзя делить на ноль")
           continue
       print(f"x / y = {x / y}")
   else:
       print(f"x * y = {x * y}")

# Вычислить результат Z в зависимости от знака.
# Предусмотреть реакции на возможный неверный знак операции, а также на ввод Y=0 при делении.
# Организовать возможность многократных вычислений без перезагрузки программа (т.е. построить бесконечный цикл).
# В качестве символа прекращения вычислений принять ‘0’ (т.е. sign='0').