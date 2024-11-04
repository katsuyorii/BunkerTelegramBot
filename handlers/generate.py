from aiogram import Router, F
from aiogram.types import Message

from settings import BUTTONS_NAMES


router = Router()


@router.message(F.text == BUTTONS_NAMES['character'])
async def command_character(message: Message):
    ''' Функция обработки кнопки генерации «Персонаж» '''
    await message.answer('char')


@router.message(F.text == BUTTONS_NAMES['catastrophe'])
async def command_catastrophe(message: Message):
    ''' Функция обработки кнопки генерации «Катастрофа» '''
    await message.answer('catastrophe')


@router.message(F.text == BUTTONS_NAMES['bunker'])
async def command_bunker(message: Message):
    ''' Функция обработки кнопки генерации «Бункер» '''
    await message.answer('bunker')


@router.message(F.text == BUTTONS_NAMES['review_generate'])
async def command_review_generate(message: Message):
    ''' Функция обработки кнопки генерации «Обзор генераций» '''
    await message.answer('review_generate')