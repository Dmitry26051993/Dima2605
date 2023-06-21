import telebot
import requests
import json
mybot = telebot.TeleBot("6039401674:AAEU7IGyRUUG8cSJ9_cKp8VAyLB0CVN2xLw")
API = "e6921c1a4bce6a003e03e68d1d6b71e4"


@mybot.message_handler(commands=['start'])
def start(message):
    mybot.send_message(message.chat.id, "Привет) Укажи свой город)")

@mybot.message_handler(content_types=["text"])
def weather(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    data = json.loads(res.text)
    temp =data['main']['temp']
    mybot.reply_to(message, f"Сейчас погода: {temp}")
    image = 'sun.png' if temp > 5.0 else 'sky.jpg'
    file = open('./' + image, 'rb')
    mybot.send_photo(message.chat.id, file)

mybot.polling(none_stop=True)