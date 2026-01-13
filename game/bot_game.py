import asyncio
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

load_dotenv()
token = os.getenv("BOT_TOKEN")

if not token:
    print("Токена нет (BOT_TOKEN)")
    raise SystemExit(1)

dp = Dispatcher()

# состояние квеста по пользователям
user_scene = {}


def main_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Начать квест", callback_data="menu:start")],
        [InlineKeyboardButton(text="📜 Правила", callback_data="menu:rules")],
    ])


def scene1_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚪 Открыть дверь", callback_data="s1:door")],
        [InlineKeyboardButton(text="🪟 Осмотреть окно", callback_data="s1:window")],
    ])


def restart_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔁 Начать заново", callback_data="menu:start")],
        [InlineKeyboardButton(text="🏠 В меню", callback_data="menu:home")],
    ])


@dp.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    user_scene.pop(user_id, None)

    await message.answer(
        "Привет! Это мини-квест. Всё управление — кнопками 👇",
        reply_markup=main_menu_kb()
    )


@dp.callback_query(F.data.startswith("menu:"))
async def menu_handler(callback: CallbackQuery):
    user_id = callback.from_user.id
    action = callback.data.split(":", 1)[1]

    if action == "home":
        user_scene.pop(user_id, None)
        await callback.message.answer("Меню 👇", reply_markup=main_menu_kb())

    elif action == "rules":
        await callback.message.answer(
            "Правила:\n"
            "1) Жми кнопки\n"
            "2) Можно начать заново\n"
            "3) Есть концовки 😉",
            reply_markup=main_menu_kb()
        )

    elif action == "start":
        user_scene[user_id] = "scene1"
        await callback.message.answer(
            "СЦЕНА 1:\n"
            "Ты проснулся в незнакомой комнате. Свет мигает.\n"
            "Что делаешь?",
            reply_markup=scene1_kb()
        )

    await callback.answer()


@dp.callback_query(F.data.startswith("s1:"))
async def scene1_handler(callback: CallbackQuery):
    user_id = callback.from_user.id

    if user_scene.get(user_id) != "scene1":
        await callback.message.answer("Сначала нажми /start 🙂", reply_markup=main_menu_kb())
        await callback.answer()
        return

    choice = callback.data.split(":", 1)[1]

    if choice == "door":
        user_scene[user_id] = "end_bad"
        await callback.message.answer(
            "Ты открыл дверь… и включилась сигнализация.\n"
            "Концовка: 🔥 «Пойман на первой минуте»",
            reply_markup=restart_kb()
        )

    elif choice == "window":
        user_scene[user_id] = "end_good"
        await callback.message.answer(
            "Ты подошёл к окну и заметил пожарную лестницу.\n"
            "Концовка: 🧠 «Побег умом»",
            reply_markup=restart_kb()
        )

    await callback.answer()


async def main():
    bot = Bot(token=token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
