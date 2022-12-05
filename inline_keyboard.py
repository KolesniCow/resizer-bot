from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


for_telegram_sticker_button = InlineKeyboardButton(
    '500x500 For Telegram Stickers',
    callback_data='for_telegram_stickers'
)

youre_format = InlineKeyboardButton(
    'You`re format',
    callback_data='youre_format'
)

select_size_keyboard = InlineKeyboardMarkup()
select_size_keyboard.add(for_telegram_sticker_button)
select_size_keyboard.add(youre_format)
