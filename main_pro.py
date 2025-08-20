# main.py
import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, \
    FSInputFile
from dotenv import load_dotenv, find_dotenv

load_dotenv()
load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv('TOKEN')

# Callback данные для основного меню
ABOUT_CB = "about"
SERVICES_CB = "services"
DOCTORS_CB = "doctors"
CONTACTS_CB = "contacts"
BACK_TO_MAIN_CB = "back_to_main"
BACK_TO_DOCTORS_CB = "back_to_doctors"

# Callback данные для специалистов
DOCTOR_ZAITSEVA_CB = "doctor_zaitseva"
DOCTOR_DZYUBINA_CB = "doctor_dzyubina"
DOCTOR_ALTYNBEKOVA_CB = "doctor_altynbekova"
DOCTOR_SHESTAKOVA_CB = "doctor_shestakova"
DOCTOR_POPOVA_CB = "doctor_popova"
DOCTOR_GADZHIEVA_CB = "doctor_gadzhieva"
DOCTOR_KRIVOSHCHAPOVA_CB = "doctor_krivoshchapova"

# Данные специалистов
DOCTORS_DATA = {
    DOCTOR_ZAITSEVA_CB: {
        "name": "Зайцева Оксана Александровна",
        "photo_path": "photos/zaitseva.jpeg",  # Путь к фотографии
        "description": (
            "<b>Зайцева Оксана Александровна</b>\n\n"
            "🕐 <b>Стаж:</b> 24 года\n"
            "👩‍⚕️ <b>Специализация:</b> Общая врачебная практика (семейная медицина), классическая гомеопатия\n\n"
            "🎓 <b>Образование и практика:</b>\n\n"
            "• <b>2001 г.</b> – Диплом по специальности «Лечебное дело», Челябинский государственный институт\n\n"
            "• <b>2002 г.</b> – Интернатура по терапии\n\n"
            "• <b>2012 г.</b> – Профессиональная переподготовка по программе «Общая врачебная практика (семейная медицина)»\n\n"
            "• <b>2018 г.</b> – Повышение квалификации по программе «Общая врачебная практика (семейная медицина)»\n\n"
            "📋 Имеет действующий сертификат по специальности «Общая врачебная практика (семейная медицина)»\n\n"
            "• <b>С 2022 г.</b> по настоящее время обучение в Международной Академии Классической Гомеопатии Джорджа Витулкаса (Греция)"
        )
    },
    DOCTOR_DZYUBINA_CB: {
        "name": "Дзюбина Елена Николаевна",
        "photo_path": "photos/dzyubina.jpeg",
        "description": (
            "<b>Дзюбина Елена Николаевна</b>\n\n"
            "🕐 <b>Стаж:</b> 49 лет\n"
            "👩‍⚕️ <b>Специализация:</b> Классическая гомеопатия\n\n"
            "🎓 <b>Образование и практика:</b>\n\n"
            "• <b>1976 г.</b> – Диплом по специальности «Лечебное дело», Челябинский государственный институт\n\n"
            "• <b>1977 г.</b> – Окончила интернатуру по специальности «Терапевт»\n\n"
            "• <b>2008-2009 гг.</b> – Повышение квалификации по программе «Основы гомеопатии»\n\n"
            "• <b>2013 г.</b> – Повышение квалификации по программе «Актуальные вопросы гомеопатии»\n\n"
            "• <b>2015 г.</b> – Переподготовка по специальности «Общая врачебная практика (Семейная медицина)»\n\n"
            "• <b>2015 г.</b> – Повышение квалификации по программе «Организация здравоохранения и общественное здоровье»\n\n"
            "• <b>2017 г.</b> – Повышение квалификации по программе «Классическая гомеопатия»"
        )
    },
    DOCTOR_ALTYNBEKOVA_CB: {
        "name": "Алтынбекова Ольга Сергеевна",
        "photo_path": "photos/altynbekova.png",
        "description": (
            "<b>Алтынбекова Ольга Сергеевна</b>\n\n"
            "🕐 <b>Стаж:</b> 14 лет\n"
            "👩‍⚕️ <b>Специализация:</b> Организация здравоохранения и общественное здоровье, мануальная терапия, иглорефлексотерапия\n\n"
            "🎓 <b>Образование и практика:</b>\n\n"
            "• <b>2011 г.</b> – Диплом по специальности «Лечебное дело», Челябинская государственная медицинская академия\n\n"
            "• <b>2012 г.</b> – Интернатура по терапии\n\n"
            "• <b>2015 г.</b> – Профессиональная переподготовка «Организация здравоохранения и общественное здоровье»\n\n"
            "• <b>2016 г.</b> – Профессиональная переподготовка «Мануальная терапия»\n\n"
            "• <b>2020 г.</b> – Повышение квалификации «Организация здравоохранения и общественное здоровье»\n\n"
            "• <b>2020-2022 гг.</b> – Авторская программа А.А. Шлыкова «Перцептивно-мануальные техники в оздоровительной практике»\n\n"
            "• <b>2021 г.</b> – Профессиональная переподготовка «Рефлексотерапия»\n\n"
            "• <b>2021 г.</b> – Повышение квалификации «Мануальная терапия»\n\n"
            "📋 Действующие сертификаты: организация здравоохранения и общественное здоровье, мануальная терапия, рефлексотерапия\n\n"
            "• <b>С 2022 г.</b> по настоящее время обучение в Международной Академии Классической Гомеопатии Джорджа Витулкаса (Греция)"
        )
    },
    DOCTOR_SHESTAKOVA_CB: {
        "name": "Шестакова Елизавета Владимировна",
        "photo_path": "photos/shestakova.jpg",
        "description": (
            "<b>Шестакова Елизавета Владимировна</b>\n\n"
            "🕐 <b>Стаж:</b> 11 лет\n"
            "👩‍⚕️ <b>Специализация:</b> Физическая реабилитация, сестринское дело, клинический (медицинский) психолог\n\n"
            "🎓 <b>Образование и практика:</b>\n\n"
            "• <b>2009-2014 гг.</b> – ФГБОУ «УралГУФК», Специалист по адаптивной физической культуре, специализация «Физическая реабилитация»\n\n"
            "• <b>2014-2018 гг.</b> – ГБПОУ «ЧМК», Медицинская сестра, специализация «Сестринское дело»\n\n"
            "• <b>2021-2023 гг.</b> – Магистратура «Психология», специализация «Клинический (медицинский) психолог»\n\n"
            "• <b>2019 г.</b> – Медицинский массаж в педиатрии, Учебный центр ЛДА\n\n"
            "• <b>2022 г.</b> – 1,2,3 модули курса Нейровзлет Н.С. Садырова «Нейропсихология детского возраста», ООО «Толиман»\n\n"
            "• <b>2022 г.</b> – Нейропсихологическая диагностика, реабилитация и коррекция в детском возрасте А.В. Цветков\n\n"
            "• <b>С 2022 г.</b> по настоящее время – Авторская программа А.А. Шлыкова «Перцептивно-мануальные техники в оздоровительной практике»\n\n"
            "• <b>2021 г.</b> – Терапевтическое тейпирование. Базовый курс. Терапия боли и отёка\n\n"
            "• <b>2020-2023 гг.</b> – Множественные специализированные курсы по детской реабилитации, массажу и нейропсихологии"
        )
    },
    DOCTOR_POPOVA_CB: {
        "name": "Попова Алиса Владимировна",
        "photo_path": "photos/popova.jpg",
        "description": (
            "<b>Попова Алиса Владимировна</b>\n\n"
            "🕐 <b>Стаж:</b> 17 лет\n"
            "👩‍⚕️ <b>Специализация:</b> Мануальная терапия, кинезиология, рефлексотерапия, врач-педиатр\n\n"
            "🎓 <b>Образование и практика:</b>\n\n"
            "• <b>2008 г.</b> – Челябинская государственная медицинская академия, специальность «Педиатрия»\n\n"
            "• <b>2009 г.</b> – Интернатура по специальности «Педиатрия» на кафедре детских болезней и поликлинической педиатрии\n\n"
            "• <b>2017 г.</b> – Санкт-Петербургский институт гештальта, консультант в гештальт подходе\n\n"
            "• <b>2019 г.</b> – ЧУ ДПО Институт переподготовки и повышения квалификации специалистов здравоохранения по специальности «Физиотерапия»\n\n"
            "• <b>2020 г.</b> – ЧУ ДПО Институт переподготовки и повышения квалификации специалистов здравоохранения по специальности «Педиатрия»\n\n"
            "• <b>2022 г.</b> – Авторская программа А.А. Шлыкова «Перцептивно-мануальные техники в оздоровительной практике»\n\n"
            "• <b>2023 г.</b> – Профессиональная переподготовка по специальности «Врач-мануальный терапевт» ЧУ ДПО «Академия медицинской кинезиологии и мануальной терапии», г. Москва"
        )
    },
    DOCTOR_GADZHIEVA_CB: {
        "name": "Гаджиева Зарема Джумаевна",
        "photo_path": "photos/gadzhieva.jpg",
        "description": (
            "<b>Гаджиева Зарема Джумаевна</b>\n\n"
            "🕐 <b>Стаж:</b> 15 лет\n"
            "👩‍⚕️ <b>Специализация:</b> Медицинский массаж\n\n"
            "🎓 <b>Образование и практика:</b>\n\n"
            "• <b>2010 г.</b> – ФГОУ СПО «Ессентукский медицинский колледж» Минздравсоцразвития России\n\n"
            "• <b>2018 г.</b> – ФГБ ПОУ «Кисловодский медицинский колледж» Минздрава России, Медицинский массаж в педиатрии\n\n"
            "• <b>2018 г.</b> – ФГБ ПОУ «Кисловодский медицинский колледж» Минздрава России, Повышение квалификации «Медицинский массаж»\n\n"
            "• <b>2023 г.</b> – ООО «Московская академия профессионального образования»\n\n"
            "• <b>2021 г.</b> – Сертификат «Биомеханика человека» ООО «Международная академия медицинской реабилитации»\n\n"
            "• <b>2020 г.</b> – Сертификат «Бобат-терапия» ООО «Международная академия медицинской реабилитации»"
        )
    },
    DOCTOR_KRIVOSHCHAPOVA_CB: {
        "name": "Кривощапова Нелли Амиргалеевна",
        "photo_path": "photos/krivoshchapova.png",
        "description": (
            "<b>Кривощапова Нелли Амиргалеевна</b>\n\n"
            "🕐 <b>Стаж:</b> 15 лет\n"
            "👩‍⚕️ <b>Специализация:</b> Психолог\n\n"
            "🎓 <b>Образование и практика:</b>\n\n"
            "• <b>2010 г.</b> – Южно-Уральский государственный медицинский университет Министерства здравоохранения РФ\n\n"
            "• <b>2011-2013 гг.</b> – «Акушерство и гинекология» интернатура и ординатура\n\n"
            "• <b>2018 г.</b> – Первичная специализация по специальности «Врач ультразвуковой диагностики»\n\n"
            "• <b>2022 г.</b> – Первичная специализация специалист «Организации здравоохранения»\n\n"
            "• <b>2024 г.</b> – Сертификат института «Эгоресурс» по работе с метафорическими ассоциативными картами\n\n"
            "• <b>2025 г.</b> – Дополнительное профессиональное образование специалист психолог-консультант, супервизор\n\n"
            "• <b>2025 г.</b> – Повышение квалификации «Работа с посттравмой методом ДПДГ»"
        )
    }
}


# Функции для создания клавиатур
def main_menu_kb() -> InlineKeyboardMarkup:
    """Главное меню бота"""
    buttons = [
        [InlineKeyboardButton(text="О клинике", callback_data=ABOUT_CB)],
        [InlineKeyboardButton(text="Услуги и цены", callback_data=SERVICES_CB)],
        [InlineKeyboardButton(text="Специалисты", callback_data=DOCTORS_CB)],
        [InlineKeyboardButton(text="Контакты", callback_data=CONTACTS_CB)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def doctors_menu_kb() -> InlineKeyboardMarkup:
    """Меню выбора специалистов"""
    buttons = [
        [InlineKeyboardButton(text="Зайцева Оксана Александровна", callback_data=DOCTOR_ZAITSEVA_CB)],
        [InlineKeyboardButton(text="Дзюбина Елена Николаевна", callback_data=DOCTOR_DZYUBINA_CB)],
        [InlineKeyboardButton(text="Алтынбекова Ольга Сергеевна", callback_data=DOCTOR_ALTYNBEKOVA_CB)],
        [InlineKeyboardButton(text="Шестакова Елизавета Владимировна", callback_data=DOCTOR_SHESTAKOVA_CB)],
        [InlineKeyboardButton(text="Попова Алиса Владимировна", callback_data=DOCTOR_POPOVA_CB)],
        [InlineKeyboardButton(text="Гаджиева Зарема Джумаевна", callback_data=DOCTOR_GADZHIEVA_CB)],
        [InlineKeyboardButton(text="Кривощапова Нелли Амиргалеевна", callback_data=DOCTOR_KRIVOSHCHAPOVA_CB)],
        [InlineKeyboardButton(text="🔙 Назад", callback_data=BACK_TO_MAIN_CB)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def doctor_detail_kb() -> InlineKeyboardMarkup:
    """Клавиатура для страницы отдельного врача"""
    buttons = [
        [InlineKeyboardButton(text="🔙 К специалистам", callback_data=BACK_TO_DOCTORS_CB)],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data=BACK_TO_MAIN_CB)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


# Хэндлеры
async def start_handler(message: Message):
    """Обработчик команды /start"""
    await message.answer(
        "Здравствуйте! Это чат-бот клиники АСКО-Здоровье.\n\n"
        "Выберите интересующий вас раздел:",
        reply_markup=main_menu_kb()
    )


async def on_about(call: CallbackQuery):
    """Обработчик кнопки 'О клинике'"""
    await call.answer()
    text = (
        "<b>🏥 О клинике «АСКО-Здоровье»</b>\n\n"
        "Клиника «АСКО-Здоровье» создана в 2011 году под эгидой "
        "страховой компании АСКО-СТРАХОВАНИЕ с целью "
        "обеспечения высокого качества обслуживания "
        "застрахованных.\n\n"
        "Партнерство со страховой компанией позволило "
        "центру сформировать особенный подход к лечению "
        "пациентов, заключающийся во внимательном отношении "
        "к их проблемам и бережном обращении с теми "
        "возможностями, которые предоставляет застрахованному "
        "страховой полис.\n\n"
        "Сегодня «АСКО-Здоровье» — это клиника "
        "холистической медицины.\n\n"
        "Во главе такого подхода стоит индивидуальный подход "
        "к пациенту.\n\n"
        "<b>⏰ Время приема обращения граждан</b>\n"
        "Главный врач: +7 (351) 737-01-96\n"
        "Email: info@ackohealth.ru\n"
        "Среда: 10:00-12:00\n"
        "Суббота, Воскресенье — выходные дни"
    )
    await call.message.edit_text(text, parse_mode=ParseMode.HTML, reply_markup=main_menu_kb())


async def on_services(call: CallbackQuery):
    """Обработчик кнопки 'Услуги и цены'"""
    await call.answer()
    text = (
        "<b>💼 Услуги и цены</b>\n\n"
        "Уточняйте стоимость услуг у администратора.\n\n"
        "📞 Телефон для справок: +7 (351) 737-01-96"
    )
    await call.message.edit_text(text, parse_mode=ParseMode.HTML, reply_markup=main_menu_kb())


async def on_doctors(call: CallbackQuery):
    """Обработчик кнопки 'Специалисты'"""
    await call.answer()
    text = (
        "<b>👩‍⚕️ Наши специалисты</b>\n\n"
        "Выберите врача для получения подробной информации:"
    )
    await call.message.edit_text(text, parse_mode=ParseMode.HTML, reply_markup=doctors_menu_kb())


async def on_contacts(call: CallbackQuery):
    """Обработчик кнопки 'Контакты'"""
    await call.answer()
    text = (
        "<b>📍 Контакты</b>\n\n"
        "<b>Адрес:</b> г. Челябинск, ул. Первой Пятилетки, 33\n\n"
        "<b>Телефон:</b> +7 (351) 737-01-96\n\n"
        "<b>Сайт:</b> https://ackohealth.ru/\n\n"
        "<b>Email:</b> info@ackohealth.ru"
    )
    await call.message.edit_text(text, parse_mode=ParseMode.HTML, reply_markup=main_menu_kb())


# Отдельные обработчики для каждого врача
async def on_doctor_zaitseva(call: CallbackQuery):
    """Обработчик для Зайцевой О.А."""
    await call.answer()
    await show_doctor_info(call, DOCTOR_ZAITSEVA_CB)


async def on_doctor_dzyubina(call: CallbackQuery):
    """Обработчик для Дзюбиной Е.Н."""
    await call.answer()
    await show_doctor_info(call, DOCTOR_DZYUBINA_CB)


async def on_doctor_altynbekova(call: CallbackQuery):
    """Обработчик для Алтынбековой О.С."""
    await call.answer()
    await show_doctor_info(call, DOCTOR_ALTYNBEKOVA_CB)


async def on_doctor_shestakova(call: CallbackQuery):
    """Обработчик для Шестаковой Е.В."""
    await call.answer()
    await show_doctor_info(call, DOCTOR_SHESTAKOVA_CB)


async def on_doctor_popova(call: CallbackQuery):
    """Обработчик для Поповой А.В."""
    await call.answer()
    await show_doctor_info(call, DOCTOR_POPOVA_CB)


async def on_doctor_gadzhieva(call: CallbackQuery):
    """Обработчик для Гаджиевой З.Д."""
    await call.answer()
    await show_doctor_info(call, DOCTOR_GADZHIEVA_CB)


async def on_doctor_krivoshchapova(call: CallbackQuery):
    """Обработчик для Кривощаповой Н.А."""
    await call.answer()
    await show_doctor_info(call, DOCTOR_KRIVOSHCHAPOVA_CB)


async def show_doctor_info(call: CallbackQuery, doctor_key: str):
    """Универсальная функция для отображения информации о враче"""
    doctor = DOCTORS_DATA[doctor_key]
    photo_path = doctor["photo_path"]
    description = doctor["description"]

    try:
        # Попытка отправить фото с описанием
        if os.path.exists(photo_path):
            photo = FSInputFile(photo_path)
            # Отправляем фото как новое сообщение, не удаляя предыдущее
            await call.message.answer_photo(
                photo=photo,
                caption=description,
                parse_mode=ParseMode.HTML,
                reply_markup=doctor_detail_kb()
            )
        else:
            # Если фото не найдено, редактируем текущее сообщение
            await call.message.edit_text(
                f"📷 <i>Фото временно недоступно</i>\n\n{description}",
                parse_mode=ParseMode.HTML,
                reply_markup=doctor_detail_kb()
            )
    except Exception as e:
        # В случае ошибки редактируем текущее сообщение
        await call.message.edit_text(
            description,
            parse_mode=ParseMode.HTML,
            reply_markup=doctor_detail_kb()
        )


async def back_to_main(call: CallbackQuery):
    """Возврат к главному меню"""
    await call.answer()
    text = (
        "Здравствуйте! Это чат-бот клиники АСКО-Здоровье.\n\n"
        "Выберите интересующий вас раздел:"
    )

    # Проверяем, есть ли фото в сообщении
    if call.message.photo:
        # Если сообщение с фото - отправляем новое текстовое сообщение
        await call.message.answer(text, reply_markup=main_menu_kb())
    else:
        # Если обычное текстовое сообщение - редактируем его
        try:
            await call.message.edit_text(text, reply_markup=main_menu_kb())
        except Exception:
            # В случае ошибки отправляем новое сообщение
            await call.message.answer(text, reply_markup=main_menu_kb())


async def back_to_doctors(call: CallbackQuery):
    """Возврат к списку специалистов"""
    await call.answer()
    text = (
        "<b>👩‍⚕️ Наши специалисты</b>\n\n"
        "Выберите врача для получения подробной информации:"
    )

    # Проверяем, есть ли фото в сообщении
    if call.message.photo:
        # Если сообщение с фото - отправляем новое текстовое сообщение
        await call.message.answer(text, parse_mode=ParseMode.HTML, reply_markup=doctors_menu_kb())
    else:
        # Если обычное текстовое сообщение - редактируем его
        try:
            await call.message.edit_text(text, parse_mode=ParseMode.HTML, reply_markup=doctors_menu_kb())
        except Exception:
            # В случае ошибки отправляем новое сообщение
            await call.message.answer(text, parse_mode=ParseMode.HTML, reply_markup=doctors_menu_kb())


async def main():
    """Основная функция запуска бота"""
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистрация хэндлеров основного меню
    dp.message.register(start_handler, CommandStart())
    dp.callback_query.register(on_about, F.data == ABOUT_CB)
    dp.callback_query.register(on_services, F.data == SERVICES_CB)
    dp.callback_query.register(on_doctors, F.data == DOCTORS_CB)
    dp.callback_query.register(on_contacts, F.data == CONTACTS_CB)

    # Регистрация хэндлеров специалистов
    dp.callback_query.register(on_doctor_zaitseva, F.data == DOCTOR_ZAITSEVA_CB)
    dp.callback_query.register(on_doctor_dzyubina, F.data == DOCTOR_DZYUBINA_CB)
    dp.callback_query.register(on_doctor_altynbekova, F.data == DOCTOR_ALTYNBEKOVA_CB)
    dp.callback_query.register(on_doctor_shestakova, F.data == DOCTOR_SHESTAKOVA_CB)
    dp.callback_query.register(on_doctor_popova, F.data == DOCTOR_POPOVA_CB)
    dp.callback_query.register(on_doctor_gadzhieva, F.data == DOCTOR_GADZHIEVA_CB)
    dp.callback_query.register(on_doctor_krivoshchapova, F.data == DOCTOR_KRIVOSHCHAPOVA_CB)

    # Регистрация хэндлеров навигации
    dp.callback_query.register(back_to_main, F.data == BACK_TO_MAIN_CB)
    dp.callback_query.register(back_to_doctors, F.data == BACK_TO_DOCTORS_CB)

    print("🚀 Бот запущен и готов к работе!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())