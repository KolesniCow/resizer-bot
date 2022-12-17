from aiogram.types import Message, CallbackQuery

from bot.models import bot_commands
from bot.inline_keyboard import contact_menu_markup


async def print_help(message: Message):
    await message.answer(
        ''.join(
            f'{cmd.command} - {cmd.description} \n' for cmd in bot_commands
        )
    )


async def print_about_info(message: Message):
    await message.answer(
        'Simple Telegram Bot 2022 - 2023\n'
        'Created by Alexandr Kolesnikow\n',
        reply_markup=contact_menu_markup
    )


async def simple_callback(call: CallbackQuery):
    print('Hi')
    await call.message.answer('My simple Callback')
