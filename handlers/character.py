from aiogram import Router, F
from aiogram.types import Message

from config import BUTTONS_NAMES

router_character = Router()


@router_character.message(F.text == BUTTONS_NAMES['character'])
async def command_character(message: Message):
    await message.answer('char')