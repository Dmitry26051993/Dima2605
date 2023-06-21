import telebot
import sqlite3

mybot = telebot.TeleBot("6039401674:AAEU7IGyRUUG8cSJ9_cKp8VAyLB0CVN2xLw")
name = None
@mybot.message_handler(commands=["start"])
def start(message):
    conn = sqlite3.connect("my_db.sql")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id int auto_increment primary_key, name varchar(50), pass varchar(50))")
    conn.commit()
    cur.close()
    conn.close()
    mybot.send_message(message.chat.id, "Привет) Давай сейчас зарегенимся)")
    mybot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    mybot.send_message(message.chat.id, "Введите пароль)")
    mybot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect("my_db.sql")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()
    marcup = telebot.types.InlineKeyboardMarkup()
    marcup.add(telebot.types.InlineKeyboardButton("Список пользователей", callback_data="users"))
    mybot.send_message(message.chat.id, "Все готово", reply_markup=marcup)

@mybot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect("my_db.sql")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    info = ""
    for el in users:
        info += f"name: {el[1]} password: {el[2]}\n"
    cur.close()
    conn.close()
    mybot.send_message(call.message.chat.id, info)



mybot.polling(none_stop=True)