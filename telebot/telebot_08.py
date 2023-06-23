from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
mybot = Bot("6039401674:AAEU7IGyRUUG8cSJ9_cKp8VAyLB0CVN2xLw")
db = Dispatcher(mybot)

@db.message_handler(commands=["start"])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.KeyboardButton("Открыть вебстраницу", web_app=WebAppInfo(url="https://itproger.com/")))
    await message.answer("Hello, my friend", reply_markup=markup)

executor.start_polling(db)