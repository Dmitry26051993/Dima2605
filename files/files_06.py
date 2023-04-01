# Имеются два текстовых файла с одинаковым числом строк.
# Выяснить, совпадают ли их строки.
# Если нет, то получить номер первой строки,
# в которой эти файлы отличаются друг от друга.
count = 0
eq = True
with open("text.txt", "r") as file1, open("text2.txt", "r") as file2:
    for a1, a2 in zip(file1, file2):
        count += 1
        if a1 != a2:
            eq = False
            break
print(f"Нет отличий") if eq else print(f"Отличается строка {count}")