from aiogram.types import Message
from bot.inline_keyboard import contact_menu_markup


async def menu(message: Message):
    await message.answer(
        'Showing menu...',
        reply_markup=contact_menu_markup
    )
