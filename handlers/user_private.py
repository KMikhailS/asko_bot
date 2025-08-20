from aiogram.filters import CommandStart, Command, or_f
from aiogram import types, Router, F
from keyboards import reply

user_private_router = Router()

@user_private_router.message(CommandStart())
async def echo_start(message: types.Message):
    await message.answer("Здравствуйте. Это чат бот клиники Аско-Здоровье.", reply_markup=reply.start_kb)

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