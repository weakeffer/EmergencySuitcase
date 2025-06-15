import asyncio
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hbold
from keyboards import choose_breathing_practice, get_anxiety_keyboard

callback_router = Router()

@callback_router.callback_query(F.data == "breathe")
async def handle_breathe(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(f"Выберите технику дыхания которая поможет вам успокоиться!",
                                  reply_markup=choose_breathing_practice())

@callback_router.callback_query(F.data == "back")
async def delete_message(callback:CallbackQuery):
    await callback.message.delete()

@callback_router.callback_query(F.data == "test")
async def handle_breathe(callback: CallbackQuery):
    await callback.message.answer(f"Вы можете пройти тест на уровень тревоги. "
                                  f"{hbold(callback.from_user.full_name)}", reply_markup=get_anxiety_keyboard())

@callback_router.callback_query(F.data == "daily_advice")
async def handle_breathe(callback: CallbackQuery):
    await callback.message.answer(f"Здесь ты сможешь получить совет дня, "
                                  f"{hbold(callback.from_user.full_name)}")

@callback_router.callback_query(F.data == "alarm_bell")
async def handle_breathe(callback: CallbackQuery):
    await callback.message.answer(f"Здесь ты можешь добавить экстренный контакт для звонка, "
                                  f"{hbold(callback.from_user.full_name)}")
