import io

import cv2
import numpy as np

from main import bot
from aiogram import types


def strech_image(buffer: io.BytesIO, w: int, h: int) -> bytes:
    """Stretching image in given width and higth
    Args:
        buffer (io.BytesIO): buffer with image 
        w (int): image width on output
        h (int): image height on output

    Returns:
        bytes: bytes image in format .jpg
    """
    telegram_image = cv2.imdecode(np.frombuffer(buffer.read(), np.uint8), 1)
    stratched_image = cv2.resize(telegram_image, (w, h), interpolation=cv2.INTER_LANCZOS4)
    return cv2.imencode('.jpg', stratched_image)[1].tobytes()



async def resize_photo(message: types.Message, h: int = 500, w: int = 500):
    """Downloading telegram image, which is sent to the bot, and change width and height it.

    Args:
        message (types.Message): message with photo
        h (int, optional): image height on output. Defaults to 500 becose it default sticker height px in telegram.
        w (int, optional): image width on output. Defaults to 500 becose it default sticker width px in telegram.
    
    Returns:
        Sending changed image to telegram.
    """
    file_info = await bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded = await bot.download_file(file_info.file_path)
    stretched_image = strech_image(downloaded, h=h, w=w)
    await bot.send_document(message.from_user.id, ('image.jpg', stretched_image))

