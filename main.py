import os
import logging
import asyncio
from cmath import asinh
from idlelib.undo import Command
import callback
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from keyboards import start_inline_keyboard
from dotenv import load_dotenv
from callback import callback_router
from breathing_practices import breathing_router
from anxiety_test import anxiety_router

load_dotenv()

TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main() -> None:
    bot = Bot(token=TOKEN, default = DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(callback_router)
    dp.include_router(breathing_router)
    dp.include_router(anxiety_router)

    @dp.message(Command("start"))
    async def start_command(message:Message):
        await message.answer(f"Привет, {hbold(message.from_user.full_name)}, я твой антидепрессант!"
                             f"Чем я могу тебе помочь?",
                             reply_markup=start_inline_keyboard())

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
if __name__ == '__main__':
    asyncio.run(main())