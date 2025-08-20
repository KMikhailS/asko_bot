# main.py
import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv, find_dotenv

load_dotenv()
load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv('TOKEN')

ABOUT_CB = "about"
SERVICES_CB = "services"
DOCTORS_CB = "doctors"
CONTACTS_CB = "contacts"

# 1) Построитель клавиатуры
def main_menu_kb() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="О клинике",        callback_data=ABOUT_CB)],
        [InlineKeyboardButton(text="Услуги и цены",    callback_data=SERVICES_CB)],
        [InlineKeyboardButton(text="Специалисты",      callback_data=DOCTORS_CB)],
        [InlineKeyboardButton(text="Контакты",         callback_data=CONTACTS_CB)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# 2) Хэндлер /start
async def start_handler(message: Message):
    await message.answer(
        "Здравствуйте. Это чат бот клиники Аско-Здоровье.",
        reply_markup=main_menu_kb()
    )

# 3) Обработчики нажатий кнопок
async def on_about(call: CallbackQuery):
    await call.answer()  # короткий всплывающий ответ (опционально)
    text = (
        "<b>О клинике «АСКО-Здоровье»</b>\n"
        "Клиника «АСКО-Здоровье» создана в 2011 под эгидой\n"
        "страховой компании АСКО-СТРАХОВАНИЕ с целью\n"
        "обеспечения высокого качества обслуживания\n"
        "застрахованных.\n"
        "Партнерство со страховой компаний позволило\n"
        "центру сформировать особенный подход к лечению\n"
        "пациентов, заключающийся во внимательном отношении\n"
        "к их проблемам и бережном обращении с теми\n"
        "возможностями, которые предоставляет застрахованному\n"
        "страховой полис.\n"
        "Сегодня «АСКО-Здоровье» — это клиника\n"
        "холистической медицины.\n"
        "Во главе такого подхода стоит индивидуальный подход\n"
        "к пациенту.\n"
        "<b>Время приема обращения граждан</b>\n"
        "Главный врач +7 (351) 737-01-96, info@ackohealth.ru Ср: 10:00-12:00 Сб, Вс — выходные дни"
    )
    await call.message.edit_text(text, parse_mode=ParseMode.HTML, reply_markup=main_menu_kb())

async def on_services(call: CallbackQuery):
    await call.answer()
    text = (
        "<b>Услуги и цены</b>\n"
        "Уточняйте стоимость у администратора."
    )
    await call.message.edit_text(text, parse_mode=ParseMode.HTML, reply_markup=main_menu_kb())

async def on_doctors(call: CallbackQuery):
    await call.answer()
    text = (
        "<b>Специалисты</b>\n"
    )
    await call.message.edit_text(text, parse_mode=ParseMode.HTML, reply_markup=main_menu_kb())

async def on_contacts(call: CallbackQuery):
    await call.answer()
    text = (
        "<b>Контакты</b>\n"
        "Адрес: г. Челябинск, ул. Первой Пятилетки, 33\n"
        "Телефон: +7 (351) 737-01-96\n"
        "Сайт: https://ackohealth.ru/e\n"
    )
    await call.message.edit_text(text, parse_mode=ParseMode.HTML, reply_markup=main_menu_kb())

# 4) Запуск бота
async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистрация хэндлеров
    dp.message.register(start_handler, CommandStart())
    dp.callback_query.register(on_about, F.data == "about")
    dp.callback_query.register(on_services, F.data == "services")
    dp.callback_query.register(on_doctors, F.data == "doctors")
    dp.callback_query.register(on_contacts, F.data == "contacts")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
