# Дан список целых чисел. Подсчитать сколько четных чисел в списке
a = [2, 1, 4, 80]
count = 0
for i in a:
    if i % 2 == 0:
        count += 1
print(count)
