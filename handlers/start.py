from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.reply_keyboard import main_kb
from config import COMMANDS_RESPONSES

router_start = Router()


@router_start.message(CommandStart())
async def command_start(message: Message):
    await message.answer(COMMANDS_RESPONSES['start'], reply_markup=main_kb)