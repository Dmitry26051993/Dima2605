# Дан список чисел.
# Вернуть список, где каждое число переведено в строку
# [5, 3] -> [‘5’, ‘3’]
arr = [1, 2, 3, 4, 5]
arr1 = list(map(str, arr))
print(arr1)
arr3 = [str(i) for i in arr]
print(arr3)
def my_func(i):
    return str(i)
arr4 = list(map(my_func, arr))
print(arr4)