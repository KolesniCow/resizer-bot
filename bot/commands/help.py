from aiogram.types import Message
from aiogram.filters import CommandObject

from bot.models import bot_commands
from utils import print_help


async def help_command(message: Message, command: CommandObject):
    if command.args:
        for cmd in bot_commands:
            if cmd.command == command.args:
                return await message.answer(
                    f'{cmd.command} - {cmd.description}'
                )
        await message.answer('Command is not exist')
    else:
        print_help(message)
