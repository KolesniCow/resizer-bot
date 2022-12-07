import io

import cv2
import numpy as np
from aiogram import types

from main import bot
from models import Quality, ExtensionFile, Filter


def strech_image(buffer: io.BytesIO, w: int, h: int) -> bytes:
    """Stretching image in given width and higth
    Args:
        buffer (io.BytesIO): buffer with image
        w (int): image width on output
        h (int): image height on output

    Returns:
        bytes: bytes image in format .jpg
    """
    try:
        if w != 0 and h != 0:
            telegram_image = cv2.imdecode(
                np.frombuffer(buffer.read(), np.uint8), 1
            )

            stratched_image = cv2.resize(
                telegram_image,
                (w, h),
                interpolation=cv2.INTER_LANCZOS4
            )
            print('resizing image is complite')
            return cv2.imencode('.jpg', stratched_image,
                                params=[cv2.IMWRITE_JPEG_QUALITY, 100]
                                )[1].tobytes()
        else:
            print('Width or height can`t equal 0')
            return None
    except (TypeError, ValueError, AttributeError):
        print('Error image type is not byte')
        return None


async def resize_photo(message: types.Message, h: int = 500, w: int = 500):
    """
    Downloading telegram image, which is sent to the bot,
    and change width and height it.

    Args:
        message (types.Message): message with photo
        h (int, optional): image height on output.
        Defaults to 500 becose it default sticker height px in telegram.
        w (int, optional): image width on output.
        Defaults to 500 becose it default sticker width px in telegram.

    Returns:
        stratched_image: bytes image
    """
    file_info = await bot.get_file(
        message.photo[len(message.photo) - 1].file_id
    )

    downloaded = await bot.download_file(file_info.file_path)
    stretched_image = strech_image(downloaded, h=h, w=w)
    return stretched_image


async def download_sticker(
    sticker: types.Sticker,
    quality: Quality = Quality.MEDIUM,
    extension: ExtensionFile = ExtensionFile.JPG,
    img_filter: Filter = None
):
    """Download telegram sticker

    Args:
        sticker (types.Message): sticker,
        In aiogram sticker can take with message.sticker
        quality (Quality): quality in module models
        extension (ExtensionFile): extension in module models
        img_filter (Filter): filter in module models

    Returns:
        sticker_image: bytes sticker
    """
    try:
        buffer = io.BytesIO()
        await sticker.download(destination_file=buffer)
        image = cv2.imdecode(np.frombuffer(buffer.read(), np.uint8), 1)
        image = cv2.imencode(
            extension.value,
            image,
            params=[cv2.IMWRITE_JPEG_QUALITY, quality.value]
        )[1].tobytes()
        return image
    except cv2.error:
        return None
