from aiogram import Dispatcher, Bot
from .handlers import router
import os

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()
dp.include_router(router)

async def main():
    await dp.start_polling(bot)