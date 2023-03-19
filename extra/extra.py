# Есть список
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
a = 1
i = 0
while i < len(arr):
    a *= arr[i]
    i = i + 1
print(pow(a, 1 / len(arr)))
# 4. Найти массив квадратов.
i = 0
while i < len(arr):
    arr[i] = arr[i] ** 2
    i += 1
print(arr)
# 5*. Найти кумулятивную сумму
arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
i = 1
while i < len(arr):
    arr[i] = arr[i] + arr[i - 1]
    i += 1
print(arr)
# 6*. Найти медианy
arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
sorted_array = sorted(arr)
count_array = 0
while arr:
    arr.pop()
    count_array += 1
if count_array % 2 == 0:
    median = (sorted_array[count_array//2] + sorted_array[(count_array//2)-1])/2
else:
    median = sorted_array[count_array // 2]
print(median)
# 7*. Найти верхнюю и нижнюю квартиль.
arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
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
