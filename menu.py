from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_resize_button = KeyboardButton('Resize 🖼️')

menu_resize_bot = ReplyKeyboardMarkup(resize_keyboard=True)
menu_resize_bot.add(start_resize_button)
