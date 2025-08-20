from aiogram.types import BotCommand

bot_commands_private = [
    BotCommand(command="/about", description="О клинике"),
    BotCommand(command="/services", description="Услуги и цены"),
    BotCommand(command="/masters", description="Специалисты"),
    BotCommand(command="/contacts", description="Контакты")
]