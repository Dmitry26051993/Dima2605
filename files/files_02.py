# Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры.
with open("text.txt", "w") as file:
    for _ in range(6):
        text = input("Введите текст: ")
        file.write(text)
        file.write("\n")
print("--------------")
with open("text.txt") as file:
    file.close()