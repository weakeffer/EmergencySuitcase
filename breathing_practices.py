import asyncio
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hbold
from keyboards import choose_breathing_practice, repeat_for_breathing, try_technique

breathing_router = Router()

async def execute_breathing(callback: CallbackQuery, technique: str):
    try:
        await callback.message.delete()
    except:
        pass

    if technique == "square_breathing":
        steps = [
            ("🟢 Вдох", 4),
            ("🟡 Задержка", 4),
            ("🔴 Выдох", 4),
            ("🟣 Пауза", 4)
        ]
    elif technique == "breathing478":
        steps = [
            ("🟢 Вдох", 4),
            ("🟡 Задержка", 7),
            ("🔴 Выдох", 8)
        ]
    elif technique == "breathing639":
        steps = [
            ("🟢 Вдох", 4),
            ("🟡 Задержка", 7),
            ("🔴 Выдох", 8)
        ]
    elif technique == "diaphragmatic_breathing":
        steps = [
            ("🟢 Вдох", 2),
            ("🔴 Выдох", 5)
        ]
    else:
        steps = []


    msg = await callback.message.answer(f"🌀 <b>{technique.replace('_', ' ').title()}</b> начало через 3...")
    await asyncio.sleep(3)

    for step_message, sec in steps:
        for s in range(sec, 0, -1):
            await msg.edit_text(f"{step_message} : {s} сек...")
            await asyncio.sleep(1)

    await msg.edit_text(f"✅ Готово! Повторите цикл 3-5 раз."
                        f"Техника: {technique.replace('_', ' ').title()}",
                        reply_markup=repeat_for_breathing(technique))

@breathing_router.callback_query(F.data == "square_breathing")
async def square_breathing(callback : CallbackQuery):
    await callback.answer()
    try:
        await callback.message.delete()
    except:
        pass

    await callback.message.answer(
        text="🌀 <b>Квадратное дыхание</b>\n\n"
             "⭐️ <i>Популярная, простая и эффективная техника для быстрого восстановления при:</i>\n"
             "• тревоге\n• страхе\n• панических атаках\n• напряжении\n\n"
             "📝 <b>Как выполнять:</b>\n"
             "1. На 4 счета вдохнули носом\n"
             "2. На 4 счета задержали дыхание\n"
             "3. На 4 счета выдохнули ртом\n"
             "4. На 4 счета задержали дыхание\n\n"
             "⏱ <b>Продолжительность:</b>\n"
             "Повторите цикл в течение 5-15 минут\n\n"
             "✨ <b>Совет:</b>\n"
             "Для большего эффекта можно визуализировать упражнение: дышите, глядя на любой квадратный предмет "
             "и мысленно переключаясь из угла в угол\n\n"
             "⚡️ <b>Как это работает:</b>\n"
             "• При вдохе нервная система возбуждается\n"
             "• При выдохе успокаивается\n"
             "• Такая схема стабилизирует вегетативную нервную систему",
        reply_markup=try_technique("square_breathing")
    )

@breathing_router.callback_query(F.data == "breathing478")
async def breathing478(callback : CallbackQuery):
    await callback.answer()
    try:
        await callback.message.delete()
    except:
        pass
    await callback.message.answer(
        text="🌬️ <b>Дыхание 4-7-8</b>\n\n"
             "💆‍♂️ <i>Эффективная техника против стресса и тревоги</i>\n\n"
             "🔹 <b>Как выполнять:</b>\n"
             "1. Вдох на 4 счета\n"
             "2. Задержка на 7 счетов\n"
             "3. Медленный выдох на 8 счетов\n\n"
             "✨ <b>Совет:</b> Представляйте, как на выдохе уходят негативные эмоции\n\n"
             "⏱ <b>Продолжительность:</b> 10-30 циклов\n\n"
             "💤 <b>Особенно полезно:</b> Перед сном для быстрого засыпания\n\n"
             "⚡️ <b>Эффект:</b> Удлиняет выдох, что успокаивает нервную систему",
        reply_markup=try_technique("breathing478")
    )

@breathing_router.callback_query(F.data == "breathing639")
async def breathing639(callback : CallbackQuery):
    await callback.answer()
    try:
        await callback.message.delete()
    except:
        pass
    await callback.message.answer(
        text="🌪️ <b>Дыхание 6-3-9</b> - мощный антистресс\n\n"
             "🔥 <i>Экспресс-метод для мгновенного успокоения</i>\n\n"
             "🎯 <b>Техника выполнения:</b>\n"
             "1. Глубокий вдох через нос (6 сек)\n"
             "2. Короткая задержка (3 сек)\n"
             "3. Плавный выдох ртом (9 сек)\n\n"
             "🔄 <b>Рекомендуется:</b> 5-15 циклов\n\n"
             "💡 <b>Секрет эффективности:</b>\n"
             "• Удлинённый выдох (в 1.5 раза длиннее вдоха)\n"
             "• Активирует парасимпатическую систему\n"
             "• Быстро снижает уровень кортизола\n\n"
             "🌟 <b>Идеально подходит:</b>\n"
             "- Перед важными событиями\n"
             "- При остром стрессе\n"
             "- Для вечернего расслабления",
        reply_markup=try_technique("breathing639")
    )

@breathing_router.callback_query(F.data == "diaphragmatic_breathing")
async def diaphragmatic_breathing(callback : CallbackQuery):
    await callback.answer()
    try:
        await callback.message.delete()
    except:
        pass
    await callback.message.answer(
        text="🌊 <b>Диафрагмальное (брюшное) дыхание</b>\n\n"
             "🧠 <i>Естественный способ дыхания, который мы часто теряем из-за стресса</i>\n\n"
             "🔹 <b>Как выполнять:</b>\n"
             "1. Лягте на спину, слегка согнув ноги\n"
             "2. Одну руку положите на живот, другую на грудь\n"
             "3. Медленный вдох носом (1-2 сек) → живот округляется\n"
             "4. Плавный выдох ртом (3-5 сек) → живот втягивается\n\n"
             "⚠️ <b>Важно:</b> Перед практикой расслабьте плечи и шею!\n\n"
             "⚡️ <b>Физиология:</b>\n"
             "- Диафрагма двигается на 2 см вверх-вниз\n"
             "- Наполняет легкие на 80% от их емкости\n"
             "- В норме должно быть основным типом дыхания\n\n"
             "💪 <b>Эффекты:</b>\n"
             "• Снимает мышечные зажимы\n"
             "• Уменьшает тревожность\n"
             "• Улучшает кровообращение\n"
             "• Насыщает мозг кислородом\n"
             "• Нормализует давление\n\n"
             "🕯 <b>Для усиления:</b> Практикуйте 5-10 мин 2 раза в день",
        reply_markup=try_technique("diaphragmatic_breathing")
    )

@breathing_router.callback_query(F.data.startswith("repeat_"))
async def repeat_technique(callback : CallbackQuery):
    await callback.answer()
    technique = callback.data.split('_', 1)[1]
    await execute_breathing(callback, technique)

@breathing_router.callback_query(F.data.startswith("try_"))
async def try_breathing_technique(callback: CallbackQuery):
    await callback.answer()
    technique = callback.data.split("_", 1)[1]
    await execute_breathing(callback, technique)
