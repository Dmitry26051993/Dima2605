import telebot
from telebot import types
from currency_converter import CurrencyConverter
mybot = telebot.TeleBot("6039401674:AAEU7IGyRUUG8cSJ9_cKp8VAyLB0CVN2xLw")
c = CurrencyConverter()
amount = 0

@mybot.message_handler(commands=['start'])
def start(message):
    mybot.send_message(message.chat.id, "Привет введи свою сумму:")
    mybot.register_next_step_handler(message, summ)


def summ(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        mybot.send_message(message.chat.id, "Введите верное значение")
        mybot.register_next_step_handler(message, summ)
        return
    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        but1 = types.InlineKeyboardButton("EUR/USD", callback_data='eur/usd')
        but2 = types.InlineKeyboardButton("USD/EUR", callback_data='usd/eur')
        but3 = types.InlineKeyboardButton("GBP/USD", callback_data='gbp/usd')
        but4 = types.InlineKeyboardButton("USD/GBP", callback_data='usd/gbp')
        but5 = types.InlineKeyboardButton("EUR/GBP", callback_data='eur/gbp')
        but6 = types.InlineKeyboardButton("GBP/EUR", callback_data='gbp/eur')
        but7 = types.InlineKeyboardButton("Другое значение", callback_data='else')
        markup.add(but1,but2, but3, but4, but5, but6, but7)
        mybot.send_message(message.chat.id, "Выберите пару валют из представленных!", reply_markup=markup)
    else:
        mybot.send_message(message.chat.id, "Введите верное значение")
        mybot.register_next_step_handler(message, summ)

@mybot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.data != 'else':
        value = call.data.upper().split('/')
        res = c.convert(amount, value[0], value[1])
        mybot.send_message(call.message.chat.id, f"Результат {round(res, 2)}. Можете заново вписать сумму")
        mybot.register_next_step_handler(call.message, summ)
    else:
        mybot.send_message(call.message.chat.id, "Введите свою пару через слэш")
        mybot.register_next_step_handler(call.message, my_curr)

def my_curr(message):
    try:
        value = message.text.upper().split('/')
        res = c.convert(amount, value[0], value[1])
        mybot.send_message(message.chat.id, f"Результат {round(res, 2)}. Можете заново вписать сумму")
        mybot.register_next_step_handler(message, summ)
    except Exception:
        mybot.send_message(message.chat.id, f" Заново впишите сумму")
        mybot.register_next_step_handler(message, my_curr)



mybot.polling(none_stop=True)