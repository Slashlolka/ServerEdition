import logging
import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Настройка логов
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=os.getenv("7395518296:AAHV8GhlBPeuRNPLt9-kK-xxZ_JhaP7WmE4"))
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Отправь мне любое сообщение, и я его повторю!")

# Обработчик всех входящих сообщений
@dp.message_handler(content_types=ContentType.ANY)
async def echo_message(message: types.Message):
    try:
        # Создаем копию сообщения
        await message.send_copy(message.chat.id)
    except Exception as e:
        logging.error(f"Ошибка: {e}")
        await message.answer("Не могу повторить это сообщение 😢")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
