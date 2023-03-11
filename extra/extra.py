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
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
index_v_dkvar = 0.75 * (len(arr) - 1)
int_index = int(index_v_dkvar)
if index_v_dkvar % 1:
    print(arr[int_index])
else:
    result = (arr[int_index] + arr[int_index + 1]) / 2
    print(result)
index_v_dkvar = 0.25 * (len(arr) - 1)
int_index = int(index_v_dkvar)
if index_v_dkvar % 1:
    print(arr[int_index])
else:
    result = (arr[int_index] + arr[int_index + 1]) / 2
    print(result)

