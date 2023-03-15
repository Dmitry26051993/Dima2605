# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) его строки с s1-й по s2-ю;
# e) весь файл.
file = open("text.txt")
file_read = file.read()
print(file_read)
file_read_list = file_read.split()
print(file_read_list)
print(file_read_list[0], file_read_list[4], file_read_list[:5], file_read_list[0:2], file_read_list, sep="\n")
file.close()