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
count = 0

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет, мир!!!")

@dp.message(F.text)
async def echo(message: Message):
    global count
    if count == 0:
        await message.answer("Арген, завязывай страдать хуйнёй и учи Solidity")
    else:
        await message.answer(message.text)
    count += 1

async def main():
   bot = Bot(token = token)
   await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

