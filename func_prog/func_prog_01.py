# Создать lambda функцию, которая принимает на вход имя
# и выводит его в формате “Hello, {name}”
result = (lambda name: f"Hello, {name}")("Borys")
print(result)
result = lambda name: f"Hello, {name}"
print(result("Borys"))