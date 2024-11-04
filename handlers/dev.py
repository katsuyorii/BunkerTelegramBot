from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router_dev = Router()


@router_dev.message(Command('dev'))
async def command_start(message: Message):
    await message.answer('🔧 Разработчик бота - @katsuyorii')