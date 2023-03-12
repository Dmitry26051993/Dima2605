# Получить на ввод количество рублей и копеек и вывести в правильной форме.
rub = int(input("Ввести количество рублей: "))
coin = int(input("Выести количество копеек: "))
# Например, 3 рубля, 1 рубль 25 копеек, 3 копейкимер, 3 рубля, 1 рубль 25 копеек, 3 копейки
if rub and coin:
    print(f"{rub} rub. {coin} cents")
elif rub and not coin:
    print(f"{rub} rub")
else:
    print(f"{coin} cents")