import asyncio
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart

load_dotenv()
token = os.getenv("BOT_TOKEN")
if not token:
    print("Токена нет")
    raise SystemExit(1)

dp = Dispatcher()
us_count = {}
us_name = {}

@dp.message(CommandStart())
async def cmd_start(message: Message):
    us_count[message.from_user.id] = 0
    await message.answer("Привет, друг!!!")

@dp.message(F.text)
async def ansToUs(message: Message):
    if message.from_user.id not in us_count:
        us_count[message.from_user.id] = 0
    if us_count[message.from_user.id] == 0:
        await message.answer("Сначала скажи мне как тебя зовут")
    elif us_count[message.from_user.id] == 1:
        us_name[message.from_user.id] = message.text
        await message.answer(f"Завязывай страдать хуйнёй, {us_name[message.from_user.id]}, учи Solidity!!!")
    else:
        await message.answer(message.text)
    us_count[message.from_user.id] +=1

async def main():
   bot = Bot(token = token)
   await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

