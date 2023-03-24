# Дан список слов.
# Сгенерировать новый список с перевернутыми словами
arr = ["absd", "ak47", "maoe"]
print([i[::-1] for i in arr])
my_str = "dsa dsds dsad ad"
list_my_str = my_str.split()
new_list_my_str = [i[::-1]for i in list_my_str]
my_new_str = " ".join(new_list_my_str)
print(my_new_str)
arr = [i for i in range(9)]
print(arr)
new_arr = [i * 2 for i in arr]
print(new_arr)
new_arr_2 = list(map(lambda x: x * 2, arr))
print(new_arr_2, type(new_arr_2))