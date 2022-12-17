import io

import cv2
import numpy as np
from aiogram import types
import json

from main import bot
from models import Quality


def resize_image(
    buffer: io.BytesIO,
    w: int, h: int, extension: str,
    quality: Quality = Quality.MEDIUM,
) -> bytes:
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
            return cv2.imencode(extension, stratched_image,
                                params=[cv2.IMWRITE_JPEG_QUALITY, 100]
                                )[1].tobytes()
        else:
            print('Width or height can`t equal 0')
            return None
    except (TypeError, ValueError, AttributeError):
        print('Error image type is not byte')
        return None


def resize_gif(buffer: io.BytesIO, w: int, h: int):
    fourcc = cv2.VideoWriter_fourcc('G', 'I', 'F')
    cv2.VideoWriter(buffer, fourcc, 15.0, (w, h))
    return buffer


async def resize_content(
    file_info: dict, extension: str,
    content_type: str,
    h: int = 500, w: int = 500
):
    """
    Downloading telegram image, which is sent to the bot,
    and change width and height it.

    Args:
        content (types.Message.photo or .document): message with photo
        h (int, optional): image height on output.
        Defaults to 500 becose it default sticker height px in telegram.
        w (int, optional): image width on output.
        Defaults to 500 becose it default sticker width px in telegram.

    Returns:
        stratched_image: bytes image
    """
    downloaded = await bot.download_file(file_info.file_path)
    if content_type == 'photo':
        stretched_image = resize_image(
            downloaded, h=h, w=w, extension=extension
        )
        return (f'image{extension}', stretched_image)
    elif content_type == 'video':
        video = resize_gif(downloaded, h=h, w=w)
        return (f'video{extension}', video)


async def download_sticker(
    sticker: types.Sticker,
):
    """Download telegram sticker

    Args:
        sticker (types.Message): sticker,
        In aiogram sticker can take with message.sticker
        quality (Quality): quality in module models
        extension (ExtensionFile): extension in module models
        img_filter (Filter): filter in module models

    Returns:
        sticker_image: typle (file_name, bytes_image)
    """
    buffer = io.BytesIO()
    await sticker.download(destination_file=buffer)
    is_video_sticker = json.loads(sticker.as_json())['is_video']
    is_animated_sticker = json.loads(sticker.as_json())['is_animated']
    print(is_animated_sticker)
    if not is_video_sticker and not is_animated_sticker:
        return ('image.jpeg', buffer.read())
    elif is_video_sticker:
        return ('gif.gif', buffer.read())
