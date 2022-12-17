import asyncio

from aiogram import Dispatcher, Bot

from config import TOKEN
from assembly import register_commands
from models import bot_commands


async def main():
    dp = Dispatcher()
    bot = Bot(token=TOKEN)

    await bot.set_my_commands(bot_commands)
    register_commands(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
