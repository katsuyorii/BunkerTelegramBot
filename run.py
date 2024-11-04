import asyncio
import logging

from aiogram import Bot, Dispatcher

from settings import API_KEY, SKIP_UPDATE
from handlers import command, generate
from utils.commands import set_commands


bot = Bot(token=API_KEY)
dp = Dispatcher()


async def main():
    ''' Основаня функция запуска бота '''
    dp.include_routers(command.router, generate.router)

    await set_commands(bot)
    
    await bot.delete_webhook(drop_pending_updates=SKIP_UPDATE)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())