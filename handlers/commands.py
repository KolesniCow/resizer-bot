from aiogram import types

from main import dp
import menu


@dp.message_handler(commands=["start"])
async def start_bot(message: types.Message):
    '''
    Command which send message after starting bot
    '''
    await message.answer(f'Hello 👋 {message.from_user.first_name}!!!\n'
                         f'Here you will be can resize you`re images',
                         reply_markup=menu.menu_resize_bot)


@dp.message_handler(commands=["help"])
async def handler_help(message: types.Message):
    '''
    Send info about all bot command
    '''
    await message.answer('Bot given for change size you`re image \n'
                         'Commands: \n'
                         '/help - view all commands \n'
                         '/start - start bot \n'
                         '/menu - view menu\n'
                         'GLHF Bro 👏👏👏')


@dp.message_handler(commands=['menu'])
async def start_menu(message: types.Message):
    '''Comand that show menu'''
    await message.reply("Here is menu.", reply_markup=menu.menu_resize_bot)
