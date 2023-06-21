import telebot
from telebot import types


mybot = telebot.TeleBot("6039401674:AAEU7IGyRUUG8cSJ9_cKp8VAyLB0CVN2xLw")

@mybot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    but1 = types.KeyboardButton("Перейти на сайт")
    markup.row(but1)
    but2 = types.KeyboardButton("Delete photo")
    but3 = types.KeyboardButton("Изменить фото")
    markup.row(but2, but3)
    file = open("./scr.png", "rb")
    mybot.send_photo(message.chat.id, file, reply_markup=markup)
    #mybot.send_message(message.chat.id, "Hello", reply_markup=markup)
    mybot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == "Перейти на сайт":
        mybot.send_message(message.chat.id, "Website is open")
    elif message.text == "Удалить фото":
        mybot.send_message(message.chat.id, "Delete")










@mybot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton("Перейти на сайт", url="https://ezteens.com/aimee")
    markup.row(but1)
    but2 = types.InlineKeyboardButton("Delete photo", callback_data="delete")
    but3 = types.InlineKeyboardButton("Изменить фото", callback_data="update")
    markup.row(but2, but3)
    mybot.reply_to(message, "Какое красивое фото!", reply_markup=markup)


@mybot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "delete":
        mybot.delete_message(callback.message.chat.id, callback.message.message_id-1)
    elif callback.data == "update":
        mybot.edit_message_text("edit text", callback.message.chat.id, callback.message.message_id)


mybot.polling(none_stop=True)