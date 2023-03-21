# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
dct = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key in list(dct.keys()):
    dct[key + str(len(key))] = dct.pop(key)
print(dct)
dct = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
new_dict = {}
i = 0
arr = list(dct.keys())
while i < len(arr):
    new_dict[arr[i] + str(len(arr[i]))] = dct.pop(arr[i])
    i += 1
print(new_dict)

# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys()
# (подсказка: создается новый ключ с цифрой в конце, старый удаляется)
# предоставить 2 решения.
# Одно с использованием цикла while, другое с использованием цикла for с параметром.
# Оба решения предоставить в одном файле.

        