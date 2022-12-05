from aiogram.dispatcher.filters.state import StatesGroup, State


class ResizeStatesForTelegramFormat(StatesGroup):
    """
    States for resizing photo for telegram stickers size 500x500 px
    """
    get_image_for_telegram_format_state = State()


class ResizeStatesCustom(StatesGroup):
    get_image_state = State()
    get_width_state = State()
    get_height_state = State()
