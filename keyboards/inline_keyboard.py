from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ABOUT_CB = "about"
SERVICES_CB = "services"
DOCTORS_CB = "doctors"
CONTACTS_CB = "contacts"

def main_menu_kb() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="О клинике",        callback_data=ABOUT_CB)],
        [InlineKeyboardButton(text="Услуги и цены",    callback_data=SERVICES_CB)],
        [InlineKeyboardButton(text="Специалисты",      callback_data=DOCTORS_CB)],
        [InlineKeyboardButton(text="Контакты",         callback_data=CONTACTS_CB)],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)