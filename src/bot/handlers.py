from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start_message(message: Message):
    return await message.answer(
        """
        Привет, Я бот по аналитике видеороликов,
        анализируя статистику в базе данных по видеороликам я могу отвечать на твои вопросы
        Задай 1 вопрос и получи 1 ответ.
        """
    )