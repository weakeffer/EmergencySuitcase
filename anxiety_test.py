import asyncio
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hbold

from keyboards import get_answer_keyboard

class AnxietyTest(StatesGroup):
    answering = State()

questions = [
    "Я чувствую себя напряжённо и беспокойно",
    "Мне трудно расслабиться",
    "Я часто испытываю дрожь или потливость без причины",
    "Меня легко вывести из себя",
    "Я беспокоюсь о событиях, которые ещё не произошли",
    "У меня бывают приступы паники",
    "Я избегаю ситуаций, которые вызывают у меня тревогу",
    "Мне трудно заснуть из-за беспокойных мыслей",
    "Я часто чувствую усталость из-за постоянного напряжения",
    "Мне кажется, что со мной вот-вот случится что-то плохое"
]

anxiety_router = Router()

@anxiety_router.callback_query(F.data == "start_test")
async def start_anxiety_test(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(AnxietyTest.answering)
    await state.update_data(current_question=0,answers = [])
    await callback.message.answer(
        questions[0], reply_markup=get_answer_keyboard()
    )

@anxiety_router.callback_query(AnxietyTest.answering, F.data.startswith("answer_"))
async def answer_handler(callback: CallbackQuery, state: FSMContext):
    answer = int(callback.data.split("_")[1])
    data = await state.get_data()
    current_question = data["current_question"]
    answers = data["answers"]

    answers.append(answer)

    if current_question + 1 >= len(questions):
        total_result = sum(answers)
        await callback.message.answer(f"Тест пройден. Ваш результат {total_result} очков. ")
        await state.clear()
        return
    next_question = current_question + 1
    await state.update_data(current_question = next_question, answers = answers)
    await callback.message.edit_text(
        questions[next_question],
        reply_markup=get_answer_keyboard()
    )

    return