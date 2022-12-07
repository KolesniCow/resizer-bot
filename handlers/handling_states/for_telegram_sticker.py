from aiogram import types
from aiogram.dispatcher import FSMContext

from main import dp, bot
from opencv_utils import resize_photo
from state import ResizeStatesForTelegramFormat
from keyboards import menu_resize_bot


@dp.message_handler(
    state=ResizeStatesForTelegramFormat.get_image_for_telegram_format_state,
    content_types="photo"
)
async def push_resized_image_for_telegram_sticker(message: types.Message,
                                                  state: FSMContext):
    """Convert photo to 500x500 and sent him in telegram and finish state

    Args:
        message (types.Message): user message type photo
        state (FSMContext): telegram state
    """
    resized_photo = await resize_photo(message)
    await bot.send_document(
        message.from_user.id,
        ('image.jpg', resized_photo)
    )
    await bot.send_message(
        message.from_user.id,
        'Take you`re result!!!',
        reply_markup=menu_resize_bot,
    )
    await state.finish()
