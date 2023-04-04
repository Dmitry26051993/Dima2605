# В конец существующего текстового файла записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.
with open("text.txt", "a") as file:
    for _ in range(3):
        text = input("Введите текст: ")
        file.write(text)
        file.write("\n")
print("--------------")
with open("text.txt") as file:
    file.close()
with open("text.txt", "a") as file:
    s =[]
    for _ in range(3):
        text = input("Введите текст: ")
        s.append(f"{text}\n")
    file.writelines(s)
