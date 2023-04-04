# Имеются два текстовых файла с одинаковым числом строк.
# Выяснить, совпадают ли их строки.
# Если нет, то получить номер первой строки,
# в которой эти файлы отличаются друг от друга.
arr = [1, 2, 3, 4, 5, 6]
arr_1 = [11, 12, 13, 14, 15, 16]
arr_2 = [111, 122, 133, 144, 155, 166]
for el_1, el_2, el_3 in zip(arr, arr_1, arr_2):
    print(el_1, el_2, el_3)
count = 0
eq = True
with open("text.txt", "r") as file1, open("text2.txt", "r") as file2:
    for a1, a2 in zip(file1, file2):
        count += 1
        if a1 != a2:
            eq = False
            break
print(f"Нет отличий") if eq else print(f"Отличается строка {count}")


with open("text.txt", "r") as file1, open("text2.txt", "r") as file2:
    count = 1
    while line_1 := file1.readline():
        line_2 = file2.readline()
        if line_1 != line_2:
            print(f"differencec in {count} line")
            break
        count += 1


with open("text.txt", "r") as file1, open("text2.txt", "r") as file2:
    index = 1
    for line_1, line_2 in zip(file1, file2):
        if line_1 != line_2:
            print(f"differencec in {count} line")
            break
        index += 1


with open("text.txt", "r") as file1, open("text2.txt", "r") as file2:
    for index, (line_1, line_2) in enumerate(zip(file1, file2)):
        if line_1 != line_2:
            print(f"differencec in {count} line")
            break


