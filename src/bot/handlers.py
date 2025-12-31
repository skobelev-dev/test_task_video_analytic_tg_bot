from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from src.logger import logger
from src.llm import get_db_schema

router = Router()

START_MSG = """Привет, 
Я бот по аналитике видеороликов,
анализируя статистику в базе данных по видеороликам я могу отвечать на твои вопросы
Задай 1 вопрос и получи 1 ответ в виде числа)
"""


@router.message(CommandStart())
async def start_message(message: Message):
    logger.info("/start has been pressed")
    answer = await get_db_schema()
    await message.answer(answer)
    return await message.answer(START_MSG)