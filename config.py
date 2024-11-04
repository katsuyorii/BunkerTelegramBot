import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('API_KEY')
SKIP_UPDATE = os.environ.get('SKIP_UPDATE')

COMMANDS_RESPONSES = {
    'start': '''Тыры-пыры''',
    'dev': '🔧 Разработчик бота - @katsuyorii',
}

BUTTONS_NAMES = {
    'character': '👨 Персонаж',
    'catastrophe': '🛑 Катастрофа',
    'bunker': '⚠️ Бункер',
    'review_generate': '🔎 Обзор генераций',
}