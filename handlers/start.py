from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.reply_keyboard import main_kb

router_start = Router()


@router_start.message(CommandStart())
async def command_start(message: Message):
    await message.answer('Привет!')
    await message.answer('Тыры-пыры!', reply_markup=main_kb)