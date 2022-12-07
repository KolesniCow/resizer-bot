from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from models import ExtensionFile
from keyboards.skip_button import skip_button

extensions_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(extension.value) for extension in ExtensionFile
        ],
        [
            skip_button
        ]
    ]
)
