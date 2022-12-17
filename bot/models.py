from aiogram.types import BotCommand


bot_commands = [
    BotCommand(command='start', description='Start bot and show menu.'),
    BotCommand(
        command='help',
        description='Output info about commands or command.'
    ),
    BotCommand(command='menu', description='Shows menu.'),
]

MAIL_LINK = 'https://mail.google.com/mail/u/0/?fs=1&'\
            'to=alexandr.kolesnikovv2@gmail.com'\
            '&su=My%20Dear%20Friend&body=Some%20Text...&tf=cm'
