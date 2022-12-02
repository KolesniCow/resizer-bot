from aiogram import types
from aiogram.dispatcher import FSMContext

from main import dp, bot
from image import resize_photo
from state import ResizeStates

    
@dp.message_handler(state=ResizeStates.get_width_state)
async def get_width(message: types.Message, state: FSMContext):
    try:
        answer = int(message.text)
        if answer < 4000:
            await state.update_data(width=answer)
            await message.answer('Send 📏 height you`re new image:')
            await ResizeStates.get_height_state.set()
        else:
            await message.answer('It so large!!! Try again: ')
            await ResizeStates.get_width_state.set()
    except TypeError:
        await message.answer('It seems to me what it no width in pixel. Try again: ')
        await ResizeStates.get_width_state.set()
    
@dp.message_handler(state=ResizeStates.get_height_state)
async def get_height(message: types.Message, state: FSMContext):
    try:
        answer = int(message.text)
        if answer < 4000:
            await state.update_data(height=answer)
            await message.answer('Success... Now, send me you`re image')
            await ResizeStates.get_image_state.set()
        else:
            await message.answer('It so large!!! Try again: ')
            await ResizeStates.get_height_state.set()
    except TypeError:
        await message.answer('It seems to me what it no height in pixel. Try again: ')
        await ResizeStates.get_height_state.set()
    
@dp.message_handler(state=ResizeStates.get_image_state, content_types="photo")
async def push_resized_image(message: types.Message, state: FSMContext):
    height = await state.get_data('height')
    width = await state.get_data('width')
    await bot.send_message(message.from_user.id, 'Resizing process...')
    await resize_photo(message, w=width['width'], h=height['height'])
    await bot.send_message(message.from_user.id, 'Take you`re changed image.')
    await state.finish()