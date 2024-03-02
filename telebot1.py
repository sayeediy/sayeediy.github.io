
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

from config import BOT_TOKEN


bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Open Website", web_app=WebAppInfo (url='https://sayeediy.github.io/')))
    await message.answer("Hello, my friend!", reply_markup=markup)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp)
