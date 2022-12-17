from aiogram.utils.keyboard import ReplyKeyboardBuilder

main_menu = ReplyKeyboardBuilder()

main_menu.button(text='Help')
main_menu.button(text='Info')

main_menu_markup = main_menu.as_markup(resize_keyboard=True)
