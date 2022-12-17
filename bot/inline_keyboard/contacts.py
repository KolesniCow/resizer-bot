from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.models import MAIL_LINK


contact_menu = InlineKeyboardBuilder()

contact_menu.button(text='Github', url='https://github.com/KolesniCow')
contact_menu.button(text='Telegram', url='https://t.me/kolesniCow')
contact_menu.button(text='Email', url=MAIL_LINK)

contact_menu_markup = contact_menu.as_markup()
