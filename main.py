import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


logging.basicConfig(level=logging.INFO)

bot = Bot(token="token")

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())