# Создать два списка
a = [1, 2, 3, 4]
b = [ ]
# Вывести на экран id a и b
print(id(a))
print(id(b))
# Присвоить b значение a (b=a)
b = a
print(a, b)
# Вывести на экран id переменных
print(id(a))
print(id(b))
# Добавить элемент в список b
b.append(1)
print(b)
# Вывести на экран оба списка
print(a, b)
