from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram import types, Router, F
from keyboards import reply
from keyboards.inline_keyboard import (
    main_menu_kb,
    ABOUT_CB, SERVICES_CB, DOCTORS_CB, CONTACTS_CB
)

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Здравствуйте. Это чат бот клиники Аско-Здоровье.", reply_markup=main_menu_kb())

# Callbacks
@user_private_router.message(F.data == "about")
async def on_about(call: types.CallbackQuery):
    await call.answer()
    text = (
        "<b>О клинике</b>\n"
        "Современная медицинская клиника: диагностика, лечение, профилактика.\n"
        "Работаем ежедневно с 8:00 до 20:00."
    )
    await call.message.edit_text(text, parse_mode=ParseMode.HTML, reply_markup=main_menu_kb())

async def on_services(call: types.CallbackQuery):
    await call.answer()
    text = (
        "<b>Услуги и цены</b>\n"
        "Уточняйте стоимость у администратора."
    )
    await call.message.edit_text(text, parse_mode=ParseMode.HTML, reply_markup=main_menu_kb())

async def on_doctors(call: types.CallbackQuery):
    await call.answer()
    text = (
        "<b>Специалисты</b>\n"
    )
    await call.message.edit_text(text, parse_mode=ParseMode.HTML, reply_markup=main_menu_kb())

async def on_contacts(call: types.CallbackQuery):
    await call.answer()
    text = (
        "<b>Контакты</b>\n"
        "Адрес: г. Челябинск, ул. Первой Пятилетки, 33\n"
        "Телефон: +7 (351) 737-01-96\n"
        "Сайт: https://ackohealth.ru/e\n"
    )
    await call.message.edit_text(text, parse_mode=ParseMode.HTML, reply_markup=main_menu_kb())

# @user_private_router.message(CommandStart())
# async def echo_start(message: types.Message):
#     await message.answer("Здравствуйте. Это чат бот клиники Аско-Здоровье.", reply_markup=reply.start_kb)

@user_private_router.message(Command('menu'))
async def menu(message: types.Message):
    await message.answer("Меню:")

# @user_private_router.message(F.text == 'hello')
# async def menu(message: types.Message):
#     await message.answer("Это магический фильтр")

@user_private_router.message(F.text.lower() == 'о клинике')
@user_private_router.message(Command('about'))
async def about(message: types.Message):
    await message.answer("Расскажем о клинике:")

@user_private_router.message(F.text.lower() == 'услуги и цены')
@user_private_router.message(Command('services'))
async def services(message: types.Message):
    await message.answer("Расскажем об услугах и ценах")

@user_private_router.message(F.text.lower() == 'специалисты')
@user_private_router.message(Command('masters'))
async def masters(message: types.Message):
    await message.answer("Вот наши специалисты")

@user_private_router.message(F.text.lower() == 'контакты')
@user_private_router.message(Command('contacts'))
async def contacts(message: types.Message):
    await message.answer("Наши контакты")

@user_private_router.message(F.contact)
async def getContact(message: types.Message):
    await message.answer(f"Номер получен")
    await message.answer(str(message.contact))