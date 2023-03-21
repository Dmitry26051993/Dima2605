# В заданной строке расположить в обратном порядке все слова.
# Разделителями слов считаются пробелы.
my_str = input("Введите строку: ")
list = my_str.split(" ")
answer = []
for i in list:
    answer += [i[::-1]]
print(" ".join(map(str, answer)))
