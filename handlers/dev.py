from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config import COMMANDS_RESPONSES

router_dev = Router()


@router_dev.message(Command('dev'))
async def command_dev(message: Message):
    await message.answer(COMMANDS_RESPONSES['dev'])