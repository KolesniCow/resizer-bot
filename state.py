from aiogram.dispatcher.filters.state import StatesGroup, State


class ResizeStates(StatesGroup):
    get_image_for_stickers_state = State()
    get_image_state = State()
    get_width_state = State()
    get_height_state = State()
