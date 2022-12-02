from aiogram import types
from aiogram.dispatcher import FSMContext

from main import dp
from image import resize_photo
from state import ResizeStates

@dp.message_handler(state=ResizeStates.get_image_for_stickers_state, content_types="photo")
async def push_resized_imge_for_telegram_sticker(message: types.Message, state: FSMContext):
    await resize_photo(message)
    await state.finish()