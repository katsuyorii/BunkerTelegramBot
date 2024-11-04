from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='👨 Персонаж')],
    [KeyboardButton(text='🛑 Катастрофа'), KeyboardButton(text='⚠️ Бункер')],
    [KeyboardButton(text='🔎 Обзор генераций')],
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')