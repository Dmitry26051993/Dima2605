# Создать матрицу случайных чисел и сохранить ее в json файл.
# После прочесть ее, обнулить все четные элементы и сохранить в другой файл
import json
from random import randint
arr = [[randint(1, 9)for _ in range(5)]for _ in range(5)]
with open("json_1.json", "w") as file:
    data = json.dumps(arr)
    print(type(data), data)
    file.write(data)
with open("json_1.json") as file, open("json_2.json", "w") as file1:
    data = json.load(file)
    for index_row, row in enumerate(data):
        for index_number, number in enumerate(row):
            if number % 2 == 0:
                data[index_row][index_number] = 0
    print(type(data), data)
    json.dump(data, file1)


