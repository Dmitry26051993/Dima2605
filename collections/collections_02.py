# Создать список произвольного содержания.
# После каждой операции выводить список на экран
my_list = [1, 3, 34, 5,'fgr', 45]
# Добавить к нему строку “Hello”.
my_list.append('Hello')
print(my_list)
# Удалить первый элемент.
my_list.pop(0)
print(my_list)
# Поменять второй элемент на строку “World”.
my_list[1] = 'World'
print(my_list)
# Удалить элемент “World”
my_list.remove('World')
print(my_list)
# Вывести на экран перевернутый список
print(my_list[::-1])