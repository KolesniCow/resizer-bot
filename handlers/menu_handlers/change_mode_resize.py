from aiogram import types

from main import dp, bot
from state import ResizeStatesCustom, ResizeStatesForTelegramFormat


@dp.message_handler(regexp='500x500 For Telegram Stickers')
async def resize_for_telegram(message: types.Message):
    '''
    Callback for starting resize image for telegram sticker
    '''
    await bot.send_message(message.from_user.id, 'Send me you`re image')
    await ResizeStatesForTelegramFormat.get_image_for_telegram_format_state.set()


@dp.message_handler(regexp='You`re format')
async def resize_custom(message: types.Message):
    '''
    Callback for start custom resize
    '''
    await bot.send_message(
        message.from_user.id,
        'Send 📏 width you`re image:'
    )

    await ResizeStatesCustom.get_width_state.set()
