from aiogram import types

from main import dp
from keyboards import select_size_keyboard
from state import DownloadingSticker


@dp.message_handler(regexp='Resize 🖼️')
async def start_resize(message: types.Message):
    '''
    Show keyboard for choice bot mode
    '''
    await message.reply("Select size", reply_markup=select_size_keyboard)


@dp.message_handler(regexp='Download Sticker 📥')
async def download_sticker(message: types.Message):
    '''
    Start Downloading Sticker
    '''
    await message.reply("👇 Send me sticker: ")
    await DownloadingSticker.get_sticker_state.set()
