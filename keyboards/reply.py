from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="О клинике"),
            KeyboardButton(text="Услуги и цены"),
            KeyboardButton(text="Специалисты"),
            KeyboardButton(text="Контакты"),
        ],
    ],
)