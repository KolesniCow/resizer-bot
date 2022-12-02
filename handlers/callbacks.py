from aiogram import types

from main import dp, bot
from state import ResizeStates


@dp.callback_query_handler(lambda c: c.data == 'for_telegram_stickers')
async def resize_for_telegram(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Send me you`re image')
    await ResizeStates.get_image_for_stickers_state.set()
    

@dp.callback_query_handler(lambda c: c.data == 'youre_format')
async def resize_custom(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Send 📏 width you`re image:')
    await ResizeStates.get_width_state.set()