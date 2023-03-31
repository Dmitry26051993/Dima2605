# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
# где i это порядковый номер строки в списке. Использовать генератор списков.
arr = ["jdfj", "sfsf", "saas"]
new_arr = [f"{i} - {string}" for i, string in enumerate(arr)]
print(new_arr)
new_arr1 = []
for i, string in enumerate(arr):
    new_arr1.append((f"{i} - {string}"))
print(new_arr1)