from aiogram import Bot, Dispatcher, executor, types

mybot = Bot("6039401674:AAEU7IGyRUUG8cSJ9_cKp8VAyLB0CVN2xLw")
db = Dispatcher(mybot)

@db.message_handler(content_types=['photo'])
async def start(message: types.Message):
    await message.reply("Hello")

@db.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Hello", callback_data="Hello"))
    await message.reply("Hello", reply_markup=markup)

@db.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)

@db.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton("Maybe"))
    await message.answer("Hello", reply_markup=markup)
executor.start_polling(db)
