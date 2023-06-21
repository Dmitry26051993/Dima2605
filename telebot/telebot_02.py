import telebot
import webbrowser


mybot = telebot.TeleBot("6039401674:AAEU7IGyRUUG8cSJ9_cKp8VAyLB0CVN2xLw")
@mybot.message_handler(commands=['start'])
def start(message):
    mybot.send_message(message.chat.id, f"Hello {message.from_user.first_name}")

@mybot.message_handler(commands=['help'])
def start(message):
    mybot.send_message(message.chat.id, "<b>Help</b> <em><u>info</u></em>", parse_mode="html")

@mybot.message_handler(commands=['site'])
def site(message):
    webbrowser.open("https://ezteens.com/aimee")



@mybot.message_handler()
def info(message):
    if message.text.lower() == "привет":
        mybot.send_message(message.chat.id, f"Hello {message.from_user.first_name}")
    elif message.text.lower() == "id":
        mybot.reply_to(message, f"id: {message.from_user.id}")




mybot.polling(none_stop=True)


