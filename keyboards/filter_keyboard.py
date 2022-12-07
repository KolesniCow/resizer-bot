from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from models import Filter
from keyboards.skip_button import skip_button

filter_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(filter.value) for filter in Filter
        ],
        [
            skip_button
        ]
    ]
)
