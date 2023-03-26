# Описать функцию is_power_n( k , n ) логического типа, возвращающую
# True, если целый параметр k > 0 является степенью числа n > 1,
# и False в противном случае.
# Дано число n > 1 и набор из 10 целых положительных чисел.
# С помощью функции is_power_n найти количество степеней числа N в данном наборе.
import random
import math

def is_power_n(k, n):
    x = int(round(math.log(k, n)))
    if k == n**x:
        return True
    return False

def is_power_na(k, n):
    while k > 1:
        k /= n
    if k == 1.0:
        return True
    return False

s = 0
s2 = 0
n = random.randrange(2, 10)
print("N = ", n)
L = [n ** random.randrange(1, 10)+random.randrange(0, 2) for i in range(0, 10)]
for i in range(0, len(L)):
    x = L[i]
    s += int(is_power_n(x, n))
    s2 += int(is_power_na(x, n))
    print(x, ":", is_power_n(x, n), ":", is_power_na(x, n))

print("\nAmount of is_power_na:",s)
print("\nAmount of is_power_na:",s2)