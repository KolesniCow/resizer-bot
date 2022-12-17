from aiogram import Router, F
from aiogram.filters.command import Command

from bot.commands import start, help_command, menu
from bot.utils import print_help, print_about_info, simple_callback


def register_commands(router: Router) -> None:
    # Commands
    router.message.register(start, Command(commands=['start']))
    router.message.register(help_command, Command(commands=['help']))
    router.message.register(menu, Command(commands=['menu']))

    # Text
    router.message.register(print_help, F.text == 'Help')
    router.message.register(print_about_info, F.text == 'Info')

    # callbacks
    router.callback_query.register(simple_callback, F.data == 'call')
