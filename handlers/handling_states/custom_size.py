from aiogram import types
from aiogram.dispatcher import FSMContext

from main import dp, bot
from opencv_utils import resize_photo
from state import ResizeStatesCustom
from config import MAX_WIDTH, MAX_HEIGHT
from keyboards import menu_resize_bot


@dp.message_handler(state=ResizeStatesCustom.get_width_state)
async def get_width(message: types.Message, state: FSMContext):
    '''
    Get width by telegram input message, if width more than MAX_WIDTH constant,
    than will sent massage trying again,
    else will be redirect in next state get_heidht_state.
    Also check type youre message,else you sent message not with number,
    than bot also will ask you to trying again.
    '''
    try:
        answer = int(message.text)
        if answer < MAX_WIDTH and answer != 0:
            await state.update_data(width=answer)
            await message.answer('Send 📏 height you`re new image:')
            await ResizeStatesCustom.get_height_state.set()
        else:
            await message.answer(
                'It is either a lot or equal to 0.!!! Try again: '
            )
            await ResizeStatesCustom.get_width_state.set()
    except (ValueError, TypeError):
        await message.answer('It seems to me what it no width in pixel.'
                             'Try again: ')
        await ResizeStatesCustom.get_width_state.set()


@dp.message_handler(state=ResizeStatesCustom.get_height_state)
async def get_height(message: types.Message, state: FSMContext):
    '''
    Get height by telegram input message,
    if height more than MAX_HEIGHT constant,
    than will sent massage trying again,
    else will be redirect in next state get_heidht_state.
    Also check type youre message,else you sent message not with number,
    than bot also will ask you to trying again.
    '''
    try:
        answer = int(message.text)
        if answer < MAX_HEIGHT and answer != 0:
            await state.update_data(height=answer)
            await message.answer('Success... Now, send me you`re image')
            await ResizeStatesCustom.get_image_state.set()
        else:
            await message.answer(
                'It is either a lot or equal to 0.!!! Try again: '
            )
            await ResizeStatesCustom.get_height_state.set()
    except (ValueError, TypeError):
        await message.answer('It seems to me what it no height in pixel.'
                             'Try again:')
        await ResizeStatesCustom.get_height_state.set()


@dp.message_handler(
    state=ResizeStatesCustom.get_image_state, content_types="photo"
)
async def push_resized_image(message: types.Message, state: FSMContext):
    '''
    Resizing photo by height
    and widht recived in past states and send photo to user.
    '''
    height = await state.get_data('height')
    width = await state.get_data('width')
    await bot.send_message(message.from_user.id, 'Resizing process...')
    resized_photo = await resize_photo(
        message,
        w=width['width'],
        h=height['height']
    )
    await bot.send_document(message.from_user.id, ('image.jpg', resized_photo))
    await bot.send_message(
        message.from_user.id,
        'Take you`re result!!!',
        reply_markup=menu_resize_bot,
    )
    await state.finish()
