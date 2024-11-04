import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import API_KEY, SKIP_UPDATE
from handlers import start, dev
from utils.commands import set_commands


bot = Bot(token=API_KEY)
dp = Dispatcher()


async def main():
    dp.include_routers(start.router_start, dev.router_dev)
    await set_commands(bot)
    await bot.delete_webhook(drop_pending_updates=SKIP_UPDATE)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())