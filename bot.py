import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile

API_TOKEN = "8101395650:AAG-uXXy4i53Q9WYWByN6gpHczs7T78-oYg"  # Ваш токен бота
CHANNEL_USERNAME = "@transformer_people"  # Ваш Telegram-канал
CONTACT_URL = "https://t.me/klyukva1"  # Ссылка для связи и записи
AUDIO_FILE_PATH = "./Новая Медитация Покоя!.m4a"  # Путь к аудиофайлу

# Список фраз для выделения жирным (HTML-теги)
bold_phrases = [
    "Кто я и чем могу быть полезен?",
    "Коуч, гипнотерапевт, специалист по работе с подсознанием",
    "Практик осознанности и глубоких медитативных техник",
    "20+ лет опыта работы с людьми, которые хотят:",
    "Мой профессиональный путь",
    "Эриксоновский коучинг (Erickson College International)",
    "НЛП-Мастер (Институт НЛП)",
    "Эриксоновская терапия и гипноз (Институт групповой и семейной психологии)",
    "4 Quadrant Quantum Thinking (Эриксоновский колледж)",
    "Dreamwork & Advanced Metaphors (Эриксоновский колледж)",
    "Что это дает вам?",
    "Как проходит работа?",
    "Формат работы:",
    "Услуги",
    "Коучинг и психологическая поддержка",
    "Консультация (30 минут)",
    "Стандартная сессия (45 минут)",
    "Трансформационная сессия (2 часа)",
    "Основные направления:",
    "Личная психология",
    "Бизнес-психология",
    "Практики медитации",
    "Групповая медитация (8 занятий в месяц)",
    "Аудиомедитации",
    "Программа медитаций:",
    "Вторая ступень",
    "Первая ступень \"Слипер\"",
    "Готовы изменить свою жизнь?",
    "здесь и сейчас. Давайте начнем!",
    "Вторая ступень – это уже серьёзная проработка, доступ через администратора.",
    "Вторая ступень – Глубокая трансформация",
    "Эта практика выводит тебя на новый уровень осознанности и восприятия жизни.",
    "Эта медитация бесплатна – забирай и начинай практиковать прямо сейчас!",
    "держать баланс в любых ситуациях.",
    "Первая ступень – \"Слипер\"",
    "Основная цель:",
    "Аудиомедитации – твой инструмент для глубокой работы с собой",
    "Медитация – это не просто отдых.",
    "настроить сознание,",
    "Аудиомедитации – это удобно:",
    "в любое время",
    "снять стресс, сбалансировать эмоции и настроиться на ресурсное состояние",
    "глубокие изменения в мышлении, поведении и ощущении жизни",
    "Старт в июне. Количество мест строго ограничено!",
    "через тишину, благодарность и осознание момента",
    "глубокое состояние расслабления и перезагрузки",
    "Мягкая подготовка",
    "закрытая группа",
    "Как проходит практика?",
    "отпустить контроль и довериться процессу.",
    "Очищение от стресса и напряжения",
    "лёгкости, свободы и внутреннего покоя",
    "единства с природой, водой, самим собой",
    "Что ты получишь?",
    "Эта практика помогает снять напряжение на уровне тела, эмоций и ума.",
    "почувствовать связь с природой и со своим внутренним \"Я\"",
    "глубокой перезагрузки, но не получается расслабиться в обычной медитации",
    "внутреннюю усталость, напряжение или тревогу",
    "Для кого эта практика?",
    "настоящее освобождение",
    "Медитация на сапах – это особый опыт, когда ты выходишь за пределы привычного",
    "Вода — это стихия, которая несёт покой, очищение и баланс",
    "Медитация на сапах – глубокое соединение с собой через воду и дыхание",
    "Старт при наборе группы (ориентировочно с 1 апреля)",
    "погружение в состояние расслабления и осознанности",
    "Как проходят занятия?",
    "8 встреч в месяц",
    "Что даёт групповая практика?",
    "Для кого подходит?",
    "Что это такое?",
    "сильная энергетическая практика",
    "Ты можешь начать уже сейчас. Выбери подходящий формат:",
    "Медитация – это не просто расслабление.",
    "Прежде чем что-то менять в жизни, важно обрести внутреннюю опору.",
    "Медитации – фундамент твоего внутреннего баланса",
    "новых моделей поведения",
    "Хочешь выйти на новый уровень в карьере или бизнесе?",
    "Испытываешь выгорание или страх перед риском?",
    "Столкнулся с неуверенностью, прокрастинацией или недостатком мотивации?",
    "Бизнес-психология",
    "Личностная психология",
    "Медитация доступна только подписчикам канала!",
    "Вторая ступень — это глубже и мощнее.",
    "Готов(а) к глубокой трансформации?",
    "Регулярная практика усиливает эффект!",
    "Если включаешь перед сном,",
    "сидя или лёжа,",
    "в наушниках",
    "тихое место,",
    "Как использовать медитацию:",
    "Отлично! Вот твоя аудиомедитация 1-й ступени:",
    "Получить медитацию",
    "Твой подарок — аудиомедитация 1-й ступени!",
    "Чувствуешь тревогу, неуверенность или запутался в жизни?",
    "Сложно справляться со стрессом и внутренними переживаниями?",
    "Ощущение, что что-то мешает двигаться вперёд?"
]

def with_bold(text: str) -> str:
    for phrase in bold_phrases:
        text = text.replace(phrase, f"<b>{phrase}</b>")
    return text

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    # Главный экран – Приветствие и главное меню
    @dp.message(Command("start"))
    async def start_handler(message: types.Message):
        greeting = (
            "👋 Приветствую тебя! Ты на правильном пути к изменениям, и я рад, что ты здесь. Давай вместе сделаем первый шаг к твоему преобразованию.\n\n"
            "🎯 Напиши свой запрос, и мы начнем работать над твоими результатами уже с первой сессии. Ты почувствуешь перемены, и я буду рядом на каждом шагу этого пути. 🚀\n\n"
            "🎯 Выбери, что тебе нужно:"
        )
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="🎁 Подарок для тебя", callback_data="gift")],
            [types.InlineKeyboardButton(text="🧠 Личностная психология", callback_data="personal_psychology_new")],
            [types.InlineKeyboardButton(text="📊 Психология для бизнеса", callback_data="business_psychology")],
            [types.InlineKeyboardButton(text="🧘🏻‍♀️ Медитации и практики", callback_data="meditations")],
            [types.InlineKeyboardButton(text="❓ Кто я и чем помогаю", callback_data="about_me_new")],
            [types.InlineKeyboardButton(text="🔗 Подписаться на канал", url="https://t.me/transformer_people")],
            [types.InlineKeyboardButton(text="📞 Связаться с администратором", url=CONTACT_URL)]
        ])
        await message.answer(greeting, reply_markup=keyboard)

    # -------------- Подарок --------------
    @dp.callback_query(lambda c: c.data == "gift")
    async def gift_callback_handler(callback: types.CallbackQuery):
        text = (
            "🆓 Твой подарок — аудиомедитация 1-й ступени!\n"
            "Эта практика поможет расслабиться, отпустить тревожные мысли и почувствовать внутреннюю гармонию.\n\n"
            "📩 Чтобы получить медитацию, подпишись на наш Telegram-канал:\n"
            "https://t.me/transformer_people\n\n"
            "После подписки нажми кнопку \"Получить медитацию\""
        )
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="Получить медитацию", callback_data="get_meditation")]
        ])
        await callback.message.answer(with_bold(text), reply_markup=keyboard, parse_mode="HTML")
        try:
            await callback.answer()
        except Exception:
            pass

    @dp.callback_query(lambda c: c.data in ["get_meditation", "check_subscription"])
    async def get_meditation_handler(callback: types.CallbackQuery):
        try:
            chat_member = await callback.bot.get_chat_member(CHANNEL_USERNAME, callback.from_user.id)
            if chat_member.status not in ["member", "creator", "administrator"]:
                raise Exception("Not subscribed")
        except Exception:
            text = (
                "⚠️ Медитация доступна только подписчикам канала!\n"
                "📲 Подпишись на https://t.me/transformer_people, затем нажми кнопку \"Я подписался, получить медитацию\""
            )
            keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
                [types.InlineKeyboardButton(text="Я подписался, получить первую ступень", callback_data="check_subscription")]
            ])
            await callback.message.answer(with_bold(text), reply_markup=keyboard, parse_mode="HTML")
            try:
                await callback.answer("Проверьте подписку", show_alert=True)
            except Exception:
                pass
            return

        audio = FSInputFile(AUDIO_FILE_PATH)
        await callback.message.answer_audio(audio=audio)
        text = (
            "💡 Как использовать медитацию:\n"
            "- Слушай её в любое время — утром, днём или перед сном.\n"
            "- Выбери тихое место, где тебя никто не потревожит.\n"
            "- Слушай в наушниках или без них, как тебе удобнее.\n"
            "- Прими удобное положение – сидя или лёжа, главное, чтобы тело было расслаблено.\n"
            "- Включи медитацию и следуй за голосом, позволяя себе отпустить напряжение.\n\n"
            "🌙 Если уснёшь во время прослушивания, не переживай – подсознание всё равно воспримет информацию.\n\n"
            "⚡️ Регулярная практика усиливает эффект!\n\n"
            "🌀 Готов(а) к глубокой трансформации?"
        )
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="Перейти ко 2-й ступени", callback_data="go_to_second")]
        ])
        await callback.message.answer(with_bold(text), reply_markup=keyboard, parse_mode="HTML")
        try:
            await callback.answer()
        except Exception:
            pass

    @dp.callback_query(lambda c: c.data == "go_to_second")
    async def go_to_second_handler(callback: types.CallbackQuery):
        text = (
            "🔹 Вторая ступень — это глубже и мощнее.\n"
            "Она помогает снять внутренние блоки, открыть ресурсы и запустить трансформацию.\n\n"
            "💬 Оплата через администратора"
        )
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="Связаться с администратором", url=CONTACT_URL)]
        ])
        await callback.message.answer(with_bold(text), reply_markup=keyboard, parse_mode="HTML")
        try:
            await callback.answer()
        except Exception:
            pass

    # -------------- Бизнес-психология --------------
    @dp.callback_query(lambda c: c.data == "business_psychology")
    async def business_psychology_handler(callback: types.CallbackQuery):
        business_caption = (
            "🚀 Хочешь выйти на новый уровень в карьере или бизнесе?\n"
            "📌 Испытываешь выгорание или страх перед риском?\n"
            "🔍 Столкнулся с неуверенностью, прокрастинацией или недостатком мотивации?\n\n"
            "Я помогу проработать внутренние барьеры, повысить продуктивность и найти эффективные стратегии для твоего роста.\n\n"
            "Выбери формат консультации:"
        )
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="Консультация (30 минут)", callback_data="consultation_30")],
            [types.InlineKeyboardButton(text="Стандартная сессия (45 минут)", callback_data="standard_session_45")],
            [types.InlineKeyboardButton(text="Трансформационная сессия (2 часа)", callback_data="transform_session_120")]
        ])
        await callback.message.answer(with_bold(business_caption), reply_markup=keyboard, parse_mode="HTML")
        try:
            await callback.answer()
        except Exception:
            pass

    @dp.callback_query(lambda c: c.data == "consultation_30")
    async def consultation_30_handler(callback: types.CallbackQuery):
        text = (
            "🔹 ✔️ Консультация (30 минут)\n"
            "💡 Что разберём?\n"
            "- Диагностика твоей ситуации: в чём проблема и что мешает двигаться вперёд\n"
            "- Выявление ментальных барьеров и зон роста\n"
            "- Первичные рекомендации и стратегия для быстрого результата"
        )
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="Записаться на консультацию", url=CONTACT_URL)]
        ])
        await callback.message.answer(with_bold(text), reply_markup=keyboard, parse_mode="HTML")
        try:
            await callback.answer()
        except Exception:
            pass

    @dp.callback_query(lambda c: c.data == "standard_session_45")
    async def standard_session_handler(callback: types.CallbackQuery):
        text = (
            "🔹 ✔️ Стандартная сессия (45 минут)\n"
            "🔍 Что делаем?\n"
            "- Определяем глубинные ограничения и внутренние блоки\n"
            "- Выявляем скрытые ресурсы для роста\n"
            "- Разрабатываем конкретный пошаговый план без перегруза, который реально внедрить"
        )
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="Записаться на стандартную сессию", url=CONTACT_URL)]
        ])
        await callback.message.answer(with_bold(text), reply_markup=keyboard, parse_mode="HTML")
        try:
            await callback.answer()
        except Exception:
            pass

    @dp.callback_query(lambda c: c.data == "transform_session_120")
    async def transform_session_handler(callback: types.CallbackQuery):
        text = (
            "🔹 ✔️ Трансформационная сессия (2 часа)\n"
            "⚡️ Глубокая работа с подсознанием:\n"
            "- Устранение внутренних блоков, мешающих развитию в карьере или бизнесе\n"
            "- Перепрограммирование ограничивающих убеждений\n"
            "- Развитие уверенности, лидерства и стратегического мышления\n"
            "- Формирование новых моделей поведения для стабильного успеха"
        )
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="Записаться на трансформационную сессию", url=CONTACT_URL)]
        ])
        await callback.message.answer(with_bold(text), reply_markup=keyboard, parse_mode="HTML")
        try:
            await callback.answer()
        except Exception:
            pass

    # -------------- Медитации и практики --------------
    @dp.callback_query(lambda c: c.data == "meditations")
    async def meditations_handler(callback: types.CallbackQuery):
        text = (
            "🧘‍♂️ Медитации – фундамент твоего внутреннего баланса\n\n"
            "✨ Прежде чем что-то менять в жизни, важно обрести внутреннюю опору.\n"
            "Без стабильного эмоционального состояния любое решение даётся сложнее, а проблемы кажутся непреодолимыми.\n\n"
            "Медитация – это не просто расслабление.\n"
            "Это мощный инструмент для восстановления энергии, управления эмоциями и достижения осознанности.\n\n"
            "Ты можешь начать уже сейчас. Выбери подходящий формат:"
        )
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="Групповая медитация", callback_data="group_meditation")],
            [types.InlineKeyboardButton(text="Медитация на сапах", callback_data="sap_meditation")],
            [types.InlineKeyboardButton(text="Аудиомедитации", callback_data="audio_meditations")]
        ])
        await callback.message.answer(with_bold(text), reply_markup=keyboard, parse_mode="HTML")
        try:
            await callback.answer()
        except Exception:
            pass

    @dp.callback_query(lambda c: c.data == "group_meditation")
    async def group_meditation_handler(callback: types.CallbackQuery):
        text = (
            "🌿 Что это такое?\n"
            "Групповая медитация — это сильная энергетическая практика, где ты не просто работаешь над собой, но и заряжаешься общим полем участников. В группе эффект усиливается, а погружение становится глубже.\n\n"
            "💡 Для кого подходит?\n"
            "✔️ Если тебе сложно начать медитировать в одиночку\n"
            "✔️ Если нужна поддержка и вовлечённость\n"
            "✔️ Если хочешь быстрее ощутить эффект\n\n"
            "🔥 Что даёт групповая практика?\n"
            "✅ Снимает тревожность и стресс\n"
            "✅ Улучшает концентрацию и внимание\n"
            "✅ Гармонизирует внутреннее состояние\n"
            "✅ Развивает осознанность и контакт с собой\n\n"
            "🗓 Как проходят занятия?\n"
            "- 8 встреч в месяц в комфортном онлайн-формате\n"
            "- Каждое занятие — это погружение в состояние расслабления и осознанности\n"
            "- Групповая поддержка + ответы на вопросы\n\n"
            "👥 Старт при наборе группы (ориентировочно с 1 апреля)."
        )
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="Записаться в группу", url=CONTACT_URL)]
        ])
        await callback.message.answer(with_bold(text), reply_markup=keyboard, parse_mode="HTML")
        try:
            await callback.answer()
        except Exception:
            pass

    @dp.callback_query(lambda c: c.data == "sap_meditation")
    async def sap_meditation_handler(callback: types.CallbackQuery):
        text = (
            "Медитация на сапах – глубокое соединение с собой через воду и дыхание\n\n"
            "🌊 Вода — это стихия, которая несёт покой, очищение и баланс. Она мягко поддерживает тебя, снимая напряжение, забирая тревоги и возвращая в настоящий момент.\n\n"
            "Медитация на сапах – это особый опыт, когда ты выходишь за пределы привычного.\n"
            "Здесь нет стен, нет суеты, нет мыслей, которые давят изнутри. Только ты, дыхание и бесконечная гладь воды.\n\n"
            "В этом состоянии приходит настоящее освобождение – от стресса, от хаоса в голове, от усталости, которая накопилась в теле.\n\n"
            "💡 Для кого эта практика?\n"
            "✔️ Если ты чувствуешь внутреннюю усталость, напряжение или тревогу\n"
            "✔️ Если хочется глубокой перезагрузки, но не получается расслабиться в обычной медитации\n"
            "✔️ Если тебе важно почувствовать связь с природой и со своим внутренним \"Я\"\n\n"
            "🌬 Эта практика помогает снять напряжение на уровне тела, эмоций и ума.\n"
            "Ты не просто медитируешь – ты ощущаешь поддержку воды, которая несёт тебя, гармонизируя твое состояние.\n\n"
            "🔥 Что ты получишь?\n"
            "✅ Глубокий отдых на всех уровнях – физическом, эмоциональном и ментальном\n"
            "✅ Очищение от стресса и напряжения – вода мягко вытягивает всё лишнее\n"
            "✅ Чувство лёгкости, свободы и внутреннего покоя\n"
            "✅ Ощущение единства с природой, водой, самим собой\n\n"
            "Это возможность отпустить контроль и довериться процессу.\n\n"
            "🗓 Как проходит практика?\n"
            "🔹 Небольшая закрытая группа – пространство доверия и уединения\n"
            "🔹 Мягкая подготовка – дыхательные практики, настройка на состояние потока\n"
            "🔹 Ты садишься на сап-борд, вода начинает мягко покачивать тебя\n"
            "🔹 Под голос ведущего ты входишь в глубокое состояние расслабления и перезагрузки\n"
            "🔹 Возвращение к реальности через тишину, благодарность и осознание момента\n\n"
            "🏄‍♂️ Старт в июне. Количество мест строго ограничено!"
        )
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="Записаться на сап-медитацию", url=CONTACT_URL)]
        ])
        await callback.message.answer(with_bold(text), reply_markup=keyboard, parse_mode="HTML")
        try:
            await callback.answer()
        except Exception:
            pass

    @dp.callback_query(lambda c: c.data == "audio_meditations")
    async def audio_meditations_handler(callback: types.CallbackQuery):
        text = (
            "🎧 Аудиомедитации – твой инструмент для глубокой работы с собой\n\n"
            "Медитация – это не просто отдых.\n"
            "Это возможность настроить сознание, снять внутреннее напряжение и обрести ясность.\n\n"
            "📌 Аудиомедитации – это удобно:\n"
            "✔️ Ты можешь слушать их в любое время – утром, днём или перед сном\n"
            "✔️ Они помогут снять стресс, сбалансировать эмоции и настроиться на ресурсное состояние\n"
            "✔️ Регулярная практика даст глубокие изменения в мышлении, поведении и ощущении жизни"
        )
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="Первая ступень", callback_data="get_first_stage")],
            [types.InlineKeyboardButton(text="Вторая ступень", callback_data="second_stage")]
        ])
        await callback.message.answer(with_bold(text), reply_markup=keyboard, parse_mode="HTML")
        try:
            await callback.answer()
        except Exception:
            pass

    @dp.callback_query(lambda c: c.data in ["get_first_stage", "check_first_stage"])
    async def get_first_stage_handler(callback: types.CallbackQuery):
        try:
            chat_member = await callback.bot.get_chat_member(CHANNEL_USERNAME, callback.from_user.id)
            if chat_member.status not in ["member", "creator", "administrator"]:
                raise Exception("Not subscribed")
        except Exception:
            text = (
                "⚠️ Первая ступень доступна только подписчикам канала!\n"
                "📲 Подпишись на https://t.me/proverkabota123124, затем нажми кнопку \"Я подписался, получить первую ступень\""
            )
            keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
                [types.InlineKeyboardButton(text="Я подписался, получить первую ступень", callback_data="check_first_stage")]
            ])
            await callback.message.answer(with_bold(text), reply_markup=keyboard, parse_mode="HTML")
            try:
                await callback.answer("Проверьте подписку", show_alert=True)
            except Exception:
                pass
            return

        text = (
            "Первая ступень – \"Слипер\"\n"
            "🌿 Основная цель: Управление эмоциями, стабилизация психики, снижение тревожности.\n"
            "🎧 Подходит для тех, кто хочет научиться расслабляться и держать баланс в любых ситуациях.\n\n"
            "💡 Эта медитация бесплатна – забирай и начинай практиковать прямо сейчас!"
        )
        audio = FSInputFile(AUDIO_FILE_PATH)
        await callback.message.answer_audio(audio=audio)
        await callback.message.answer(with_bold(text), parse_mode="HTML")
        try:
            await callback.answer("Первая ступень отправлена!")
        except Exception:
            pass

    @dp.callback_query(lambda c: c.data == "second_stage")
    async def second_stage_handler(callback: types.CallbackQuery):
        text = (
            "Вторая ступень – Глубокая трансформация\n"
            "⚡️ Эта практика выводит тебя на новый уровень осознанности и восприятия жизни.\n"
            "Она помогает:\n"
            "✅ Разобраться с ограничивающими убеждениями\n"
            "✅ Избавиться от старых моделей мышления\n"
            "✅ Обрести внутреннюю свободу и уверенность\n\n"
            "💡 Вторая ступень – это уже серьёзная проработка, доступ через администратора."
        )
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="Перейти ко второй ступени", callback_data="go_to_second")]
        ])
        await callback.message.answer(with_bold(text), reply_markup=keyboard, parse_mode="HTML")
        try:
            await callback.answer()
        except Exception:
            pass

    # -------------- Новые обработчики для кнопок "Как я и чем помогаю" и "Личностная психология" --------------
    @dp.callback_query(lambda c: c.data == "about_me_new")
    async def about_me_handler_new(callback: types.CallbackQuery):
        text = (
            "👋 Приветствую вас друзья!  \n"
            "В жизни не бывает случайностей – если вы здесь, значит, пришло время для изменений.  \n\n"
            "<b>Кто я и чем могу быть полезен?</b>  \n\n"
            "<b>Коуч, гипнотерапевт, специалист по работе с подсознанием</b>  \n"
            "<b>Практик осознанности и глубоких медитативных техник</b>  \n"
            "<b>20+ лет опыта работы с людьми, которые хотят:</b>  \n\n"
            "🎯 Я не просто изучал психологию, коучинг и гипноз – я прошел этот путь сам. Испытав личную трансформацию, теперь помогаю другим переписать сценарии своей жизни и обрести внутренний баланс.  \n\n"
            "<b>Мой профессиональный путь</b>  \n\n"
            "<b>Эриксоновский коучинг (Erickson College International)</b> – методы глубинных изменений  \n"
            "<b>НЛП-Мастер (Институт НЛП)</b> – трансформация мышления и работа с убеждениями  \n"
            "<b>Эриксоновская терапия и гипноз (Институт групповой и семейной психологии)</b> – устранение внутренних блоков  \n"
            "<b>4 Quadrant Quantum Thinking (Эриксоновский колледж)</b> – системное мышление и квантовый подход к изменениям  \n"
            "<b>Dreamwork & Advanced Metaphors (Эриксоновский колледж)</b> – работа с бессознательными процессами через символы и метафоры  \n\n"
            "<b>Что это дает вам?</b>  \n"
            "<b>Как проходит работа?</b>  \n"
            "<b>Формат работы:</b>  \n"
            "<b>Услуги</b>  \n"
            "<b>Коучинг и психологическая поддержка</b>  \n"
            "Помогаю разобраться в сложных жизненных ситуациях, найти ресурсы и выстроить стратегию изменений.\n\n"
            "<b>Консультация (30 минут)</b>  \n"
            "💡 Диагностика вашей ситуации, выявление ключевых проблем и рекомендации.\n\n"
            "<b>Стандартная сессия (45 минут)</b>  \n"
            "🔍 В ходе сессии выявляем ключевые ограничения и недостаток ресурсов для решения задачи. Разрабатываем реалистичный пошаговый план, который будет комфортен и выполним для клиента, без перегруза и сопротивления.\n\n"
            "<b>Трансформационная сессия (2 часа)</b>  \n"
            "⚡ Работа с подсознанием: устранение внутренних блоков, трансформация ограничивающих убеждений и доступ к новым возможностям.\n\n"
            "<b>Основные направления:</b>  \n"
            "<b>Личная психология</b> – тревожность, стресс, самооценка, внутренние ограничения  \n"
            "<b>Бизнес-психология</b> – мышление предпринимателя, стратегия развития, масштабирование  \n\n"
            "<b>Практики медитации</b>  \n"
            "Эффективные методики для управления эмоциями, восстановления баланса и гармонизации внутреннего состояния.\n\n"
            "<b>Групповая медитация (8 занятий в месяц)</b>  \n"
            "🌿 Глубокие практики для осознанности и внутреннего равновесия.\n"
            "👥 Старт при наборе группы (ориентировочно с 1 апреля).\n\n"
            "<b>Аудиомедитации</b>  \n"
            "🎧 Готовые записи для расслабления, снятия стресса и перезагрузки сознания.\n\n"
            "<b>Программа медитаций:</b>  \n"
            "<b>Первая ступень \"Слипер\"</b> – управление эмоциями, стабилизация психики  \n"
            "<b>Вторая ступень</b> – глубокая трансформация, повышение осознанности  \n\n"
            "📩 Готовы изменить свою жизнь?  \n"
            "Напишите свой запрос – и мы вместе найдем лучшее решение для вас.  \n\n"
            "💡 Ваши изменения начинаются <b>здесь и сейчас. Давайте начнем!</b>  \n\n"
            "Ваш Алексей Ворожейкин  \n"
            "Эксперт по трансформации мышления и эмоционального состояния.\n\n"
            "📞 По вопросам:  \n"
            "+79372284501  \n"
            "📱 Telegram: @klyukva1"
        )
        await callback.message.answer(with_bold(text), parse_mode="HTML")
        try:
            await callback.answer()
        except Exception:
            pass

    @dp.callback_query(lambda c: c.data == "personal_psychology_new")
    async def personal_psychology_handler_new(callback: types.CallbackQuery):
        text = (
            "💭 Чувствуешь тревогу, неуверенность или запутался в жизни?\n"
            "📌 Сложно справляться со стрессом и внутренними переживаниями?\n"
            "🔍 Ощущение, что что-то мешает двигаться вперёд?\n\n"
            "Я помогу разобраться в сложных ситуациях, найти ресурсы и выстроить стратегию изменений."
        )
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="Консультация (30 минут)", callback_data="consultation_30")],
            [types.InlineKeyboardButton(text="Стандартная сессия (45 минут)", callback_data="standard_session_45")],
            [types.InlineKeyboardButton(text="Трансформационная сессия (2 часа)", callback_data="transform_session_120")]
        ])
        await callback.message.answer(with_bold(text), reply_markup=keyboard, parse_mode="HTML")
        try:
            await callback.answer()
        except Exception:
            pass

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())

