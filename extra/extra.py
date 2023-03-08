# Есть список
import statistics
arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
# 1. Найти сумму всех числел
list = len(arr)
count = 0
a = 0
while count < list:
    a = a + arr[count]
    count = count + 1
print(a)
# 2. Найти среднее арифметическое
list = len(arr)
count = 0
a = 0
while count < list:
    a = a + arr[count]
    count = count + 1
print(a / list)
# 3. Найти среднее геомнтрическое
import math
c = 1
for i in range(0, len(arr)):
    c = c * arr[i]
c1 = (float)(math.pow(c, (1 / len(arr))))
res = (float)(c1)
print(str(res))
# 4. Найти массив квадратов.
b = [i ** 2 for i in arr]
print(b)
# 5*. Найти кумулятивную сумму
cum_list = []
y = 0
for x in range(0, len(arr)):
    y += arr[x]
    cum_list.append(y)
print(cum_list)

# 6*. Найти медианy
import math
def find_median(arr):
    if len(arr) % 2 == 1:
        med = math.ceil(len(arr)/2)-1
        return arr[med]
    else:
        return -1
print(find_median(arr))
# 7*. Найти верхнюю и нижнюю квартиль

