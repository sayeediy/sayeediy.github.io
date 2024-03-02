from aiogram.types import WebAppInfo
from aiogram import types

web_app = WebAppInfo(url='https://github.com/Ali-Sayeed/telegram-web-app1')

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text='Site', web_app=web_app)]
    ],
    resize_keyboard=True
)