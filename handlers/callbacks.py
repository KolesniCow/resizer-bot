from aiogram import types

from main import dp, bot
from state import ResizeStatesCustom, ResizeStatesForTelegramFormat


@dp.callback_query_handler(lambda c: c.data == 'for_telegram_stickers')
async def resize_for_telegram(callback_query: types.CallbackQuery):
    '''
    Callback for starting resize image for telegram sticker
    '''
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Send me you`re image')
    await ResizeStatesForTelegramFormat.get_image_for_telegram_format_state.set()


@dp.callback_query_handler(lambda c: c.data == 'youre_format')
async def resize_custom(callback_query: types.CallbackQuery):
    '''
    Callback for start custom resize
    '''
    await bot.answer_callback_query(callback_query.id)

    await bot.send_message(
        callback_query.from_user.id,
        'Send 📏 width you`re image:'
    )

    await ResizeStatesCustom.get_width_state.set()
