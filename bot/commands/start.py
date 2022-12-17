from aiogram.types import Message

from reply_keyboards import main_menu_markup


async def start(message: Message):
    await message.answer(
        f'Hello, {message.from_user.first_name}',
        reply_markup=main_menu_markup
    )
