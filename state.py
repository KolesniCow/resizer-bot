from aiogram.dispatcher.state import StatesGroup, State


class ResizeStates(StatesGroup):
    get_image_state = State()
    choice_size = State()
    get_width_state = State()
    get_height_state = State()
    get_result_state = State()


class DownloadingSticker(StatesGroup):
    get_sticker_state = State()


class ProcessingStates(StatesGroup):
    get_quality_image = State()
    get_extension_image = State()
