import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_polling
from aiogram.types import ContentType
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

bot = Bot(token=os.getenv("7395518296:AAHV8GhlBPeuRNPLt9-kK-xxZ_JhaP7WmE4"))
dp = Dispatcher(bot)

async def on_startup(_):
    logging.info("Бот успешно запущен")

async def on_shutdown(_):
    logging.info("Бот остановлен")

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("👋 Привет! Просто отправь мне любое сообщение, и я его повторю!")

# Основной обработчик
@dp.message_handler(content_types=ContentType.ALL)
async def echo_all(message: types.Message):
    try:
        await message.send_copy(message.chat.id)
    except Exception as e:
        logging.error(f"Ошибка: {e}")
        await message.answer("⚠️ Не могу повторить это сообщение")

if __name__ == '__main__':
    start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown
    )
