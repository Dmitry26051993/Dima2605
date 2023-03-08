# Ввести почтовый адрес.
my_email = input("Введите Ваш имейл: ")
# Проверить доменное имя. В случае если оно gmail.com, вывести на экран имя почтового ящика.
my_list = my_email.split("@")
if "gmail.com" in my_list[-1]:
    print(my_email)
# Иначе вывести надпись “DOMAIN NAME is not supported’
else:
    print("DOMAIN NAME is not supported")