# Имеется текстовый файл.
# Переписать в другой файл все его строки с заменой в них символа 0 на символ 1 и наоборот.

with open("text.txt") as file1:
    with open("text2.txt", "w") as file2:
        a = True
        while a:
            s = ""
            a = file1.readline()
            for i in a:
                if i == "0":
                    s += "1"
                elif i == "1":
                    s += "0"
                else:
                    s += i
            file2.write(s)
