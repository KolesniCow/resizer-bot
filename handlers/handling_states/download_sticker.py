from aiogram import types
from aiogram.dispatcher import FSMContext

from main import dp, bot
from state import DownloadingSticker
from opencv_utils import download_sticker
from keyboards import menu_resize_bot


@dp.message_handler(
    state=DownloadingSticker.get_sticker_state, content_types='sticker'
)
async def download_sticker_state(message: types.Message, state: FSMContext):
    sticker = await download_sticker(message.sticker)
    if sticker != None:
        await bot.send_document(
            message.from_user.id,
            ('img.jpg', sticker)
        )
        await bot.send_message(
            message.from_user.id,
            'Take you`re sticker',
            reply_markup=menu_resize_bot
        )
    else:
        await bot.send_message(
            message.from_user.id,
            'Animated Stickers until not support',
            reply_markup=menu_resize_bot
        )
    await state.finish()
