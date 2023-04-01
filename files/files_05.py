# Имеется текстовый файл.
# Все четные строки этого файла записать во второй файл,
# а нечетные — в третий файл. Порядок следования строк сохраняется.
with open("text.txt") as file, open("text2.txt", "w") as file_1, open("text3.txt", "w") as file_2:
    lines = file.readlines()
    file_1.writelines(lines[::2])
    file_2.writelines(lines[1::2])
