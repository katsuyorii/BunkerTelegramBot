from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from settings import BUTTONS_NAMES


main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=BUTTONS_NAMES['character'])],
    [KeyboardButton(text=BUTTONS_NAMES['catastrophe']), KeyboardButton(text=BUTTONS_NAMES['bunker'])],
    [KeyboardButton(text=BUTTONS_NAMES['review_generate'])],
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')