# В заданной строке расположить в обратном порядке все слова.
my_str = str(input("Введите фразу: "))
print(my_str)
my_list = my_str.split()
print(my_list)
my_list1 = my_list[::-1]
print(my_list1)
my_str1 = " ".join(my_list1)
print(my_str1)
# Разделителями слов считаются пробелы.