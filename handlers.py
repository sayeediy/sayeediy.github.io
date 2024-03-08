

from telebot1 import bot, dp
from keyboard import keyboard
from aiogram import types
from aiogram.dispatcher.filters import Command
import config

# ... (existing code)

# Add the new imports for handling payment process
from aiogram.types import LabeledPrice
from aiogram.dispatcher import FSMContext

# Add the new functions for handling payment process
async def send_invoice(chat_id, selected_item):
    # Your logic to send an invoice
    # Use the selected_item to determine the details of the invoice
    # ...

# ... (existing code)

@dp.message_handler(content_types='web_app_data')
async def buy_process(web_app_message):
    # Ensure the correct data is received from the web app
    selected_item = web_app_message.web_app_data.data

    # Your logic to handle the payment process
    # For example, send an invoice, update the UI, etc.
    await send_invoice(web_app_message.chat.id, selected_item)

# ... (existing code)

@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_process(pre_checkout: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    await bot.send_message(message.chat.id, 'Платеж прошел успешно!')

