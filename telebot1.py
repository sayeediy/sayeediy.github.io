from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo


bot = Bot('6995587565:AAFTjc42wGPy9GDZy677tBViryb5AmD2Dz8')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Open Website", web_app=WebAppInfo (url='https://sayeediy.github.io/')))
    await message.answer("Hello, my friend!", reply_markup=markup)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)
