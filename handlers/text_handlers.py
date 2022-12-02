from aiogram import types

from main import dp
from inline_keyboard import select_size_keyboard


@dp.message_handler(regexp='Resize 🖼️')
async def start_resize(message: types.Message):
    await message.reply("Select size", reply_markup=select_size_keyboard)