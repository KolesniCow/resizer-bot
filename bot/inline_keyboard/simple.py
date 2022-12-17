from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.callback import SimpleCallbackData


simple_menu_with_callback = InlineKeyboardBuilder()

simple_menu_with_callback.button(text='Callback', callback_data=SimpleCallbackData())

simple_menu_with_callback = simple_menu_with_callback.as_markup()
