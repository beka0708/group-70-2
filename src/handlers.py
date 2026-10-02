from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import F, Router

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}, я твой первый бот!"
    )

    print(f"Пользователь {message.from_user.full_name} под ником {message.from_user.username} отправил команду /start")


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        f"/start - привествие\n"
        "/help - список команд"
    )

@router.message(F.text.lower() == "группа")
async def cmd_group(message: Message):
    await message.answer(f"Твоя группа 70-1")


@router.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")

