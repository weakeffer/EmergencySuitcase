from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def start_inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text=  "Дыхание",
        callback_data="breathe"
    ))
    builder.add(InlineKeyboardButton(
        text="Тест тревожности",
        callback_data="test"
    ))
    builder.add(InlineKeyboardButton(
        text="Совет дня",
        callback_data="daily_advice"
    ))
    builder.add(InlineKeyboardButton(
        text="Тревожный звонок",
        callback_data="alarm_bell"
    ))
    return builder.as_markup()

def choose_breathing_practice():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Квадрат",
        callback_data="square_breathing"
    ))
    builder.add(InlineKeyboardButton(
        text="Дыхание 4-7-8",
        callback_data="breathing478"
    ))
    builder.add(InlineKeyboardButton(
        text="Дыхание 6-3-9",
        callback_data="breathing639"
    ))
    builder.add(InlineKeyboardButton(
        text="Диафрагмальное дыхание",
        callback_data="diaphragmatic_breathing"
    ))
    builder.adjust(2)
    return builder.as_markup()

def repeat_for_breathing(technique:str):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text = "Повторить",
        callback_data=f"repeat_{technique}"
    ))
    builder.add(InlineKeyboardButton(
        text="Назад",
        callback_data="back"
    ))
    builder.adjust(1)
    return builder.as_markup()

def try_technique(technique: str):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Попробовать технику",
        callback_data = f"try_{technique}"
    ))
    builder.add(InlineKeyboardButton(
        text="Назад",
        callback_data="back"
    ))
    builder.adjust(1)
    return builder.as_markup()