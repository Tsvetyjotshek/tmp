from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! Для того, что бы начать работать с ботом, "
                         f"введите @CafeSpb_bot *название кафе*. Если возникнут вопросы пропишите команду /help")
