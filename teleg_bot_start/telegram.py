import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.filters.command import Command
from sql_postgress import select_last_telegram

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
TOKEN = "6594195662:AAF0Ssws8t0EzSvnjOpEHymHr4P0L6kgRr8"
PROXY_URL = "http://192.168.0.5:3128"
session = AiohttpSession(proxy=PROXY_URL)
bot = Bot(token=TOKEN, session=session)
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("price"))
async def cmd_start(message: types.Message):
    price_old = select_last_telegram()
    await message.answer(f'{price_old}')


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
