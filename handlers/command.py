from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from keyboards.reply_keyboards.main_keyboard import main_kb
from settings import COMMANDS_RESPONSES


router = Router()


@router.message(CommandStart())
async def command_start(message: Message):
    ''' Функция команды /start '''
    await message.answer(COMMANDS_RESPONSES['start'], reply_markup=main_kb)


@router.message(Command('help'))
async def command_dev(message: Message):
    ''' Функция команды /dev '''
    await message.answer(COMMANDS_RESPONSES['help'])


@router.message(Command('dev'))
async def command_dev(message: Message):
    ''' Функция команды /dev '''
    await message.answer(COMMANDS_RESPONSES['dev'])