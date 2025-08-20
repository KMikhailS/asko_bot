import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import BotCommandScopeAllPrivateChats
from dotenv import load_dotenv, find_dotenv
from keyboards.inline_keyboard import (
    main_menu_kb,
    ABOUT_CB, SERVICES_CB, DOCTORS_CB, CONTACTS_CB
)
from handlers.user_private import start_handler
from handlers.user_private import (on_about, on_services, on_doctors, on_contacts)
load_dotenv()

from common.bot_cmd_list import bot_commands_private
from handlers.user_private import user_private_router

load_dotenv(find_dotenv())
ALLOWED_UPDATES = ['message', 'edited_message']

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
dp.include_router(user_private_router)
dp.message.register(start_handler, CommandStart())
dp.callback_query.register(on_about, F.data == "about")
dp.callback_query.register(on_services, F.data == "services")
dp.callback_query.register(on_doctors, F.data == "doctors")
dp.callback_query.register(on_contacts, F.data == "contacts")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=bot_commands_private, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Shutdown requested')