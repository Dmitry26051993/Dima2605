# Создать список произвольного содержания.
# После каждой операции выводить список на экран
my_list_1 = [1, 4, 6, 7, 8]
# Создать еще один список произвольного содержания.
my_list_2 = [1, 9, 0]
# Расширить первый список вторым.
my_list_1.extend(my_list_2)
print(my_list_1)
# Вставить 123 пятым элементом.
my_list_1.insert(4, 123)
print(my_list_1)
# Вывести на экран длину итогового списка.
print(len(my_list_1))