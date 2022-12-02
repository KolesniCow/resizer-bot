import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from settings import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)


async def main():
    from handlers import dp
    await dp.bot.set_my_commands([types.BotCommand('start', 'Start bot'),types.BotCommand('help', 'Give help information'),])
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())