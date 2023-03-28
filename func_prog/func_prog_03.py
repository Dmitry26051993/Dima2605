# Дан список словарей. Каждый словарь описывает машину(серийный номер и год выпуска).
# Создать новый список со всеми машинами, год выпуска которых больше n
my_list = [{"num": 1, "year": 1993},
           {"num": 2, "year": 1997},
           {"num": 3, "year": 1995},
           {"num": 4, "year": 2003}]
n = 1996
new_list = [dict_elem for dict_elem in my_list if dict_elem["year"] > n]
print(new_list)
my_list2 = []
for elem in my_list:
    if elem["year"] > n:
        my_list2.append(elem)
print(my_list2)