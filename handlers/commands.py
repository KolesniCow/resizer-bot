from aiogram import types

from main import dp
import menu


@dp.message_handler(commands=["start"])
async def start_bot(message: types.Message):
    await message.answer(f'Hello 👋 {message.from_user.first_name}!!!\n'\
                         f'Here you will be can resize you`re images',
                         reply_markup=menu.menu_resize_bot)
    
    
@dp.message_handler(commands=["help"])
async def handler_help(message: types.Message):
    await message.answer(f'Bot given for change size you`re image \n'\
                         f'Commands: \n'\
                         f'/help - view all commands \n'\
                         f'/menu - view menu'\
                         f'GLHF Bro 👏👏👏')


@dp.message_handler(commands=['menu'])
async def start_menu(message: types.Message):
    await message.reply("Here is menu.", reply_markup=menu.menu_resize_bot)
    
