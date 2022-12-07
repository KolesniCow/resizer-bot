from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.skip_button import skip_button
from models import Quality


quality_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(quality.value) for quality in Quality
        ],
        [
            skip_button
        ]
    ]
)
