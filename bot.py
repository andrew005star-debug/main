import asyncio
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart

load_dotenv()
token = os.getenv("BOT_TOKEN")
if token is None:
    print("Токена нет")
    raise SystemExit(1)

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    # ответь пользователю текстом
    await message.answer("Привет, мир!!!")

@dp.message(F.text)
async def echo(message: Message):
    # отправь обратно то же самое, что написал пользователь
    await message.answer(message.text)

async def main():
   bot = Bot(token = token)
   await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

