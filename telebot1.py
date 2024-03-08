from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
import config


bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Open Website", web_app=WebAppInfo (url='https://sayeediy.github.io/')))
    
    
    markup.row(KeyboardButton("Manzil"), KeyboardButton("Option 2"))
    
  
    await message.answer("Hello, my friend!", reply_markup=markup)

@dp.message_handler(lambda message: message.text == "Option 2")
async def handle_option_2(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    
@dp.message_handler(lambda message: message.text == "Manzil")
async def handle_option_1(message: types.Message):
    # Send the store location
    await bot.send_location(message.chat.id, latitude=40.991672, longitude=71.667344)




if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)

