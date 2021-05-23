import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import choice_callback, otsuv_callback
from keyboards.inline.choice_buttons import choice, p_keyboard
from loader import dp, db


@dp.message_handler(Command("poll"))
async def show_items(message: Message):
    await message.answer(text="Hard Rock Cafe \n"
                              "Выберете необходиммый пункт",
                         reply_markup=p_keyboard)


@dp.callback_query_handler(choice_callback.filter(choice_name="1"))
async def chioce_one(call: CallbackQuery, callback_data: dict, statistics=3):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data}")

    await call.message.answer(f"Вы поставили этому кафе 1. Спасибо за ответ. Статистика этого кафе: {statistics}",
                              reply_markup=p_keyboard)


@dp.callback_query_handler(choice_callback.filter(choice_name="2"))
async def chioce_two(call: CallbackQuery, callback_data: dict, statistics=3):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data}")

    await call.message.answer(f"Вы поставили этому кафе 2. Спасибо за ответ. Статистика этого кафе: {statistics}",
                              reply_markup=p_keyboard)


@dp.callback_query_handler(choice_callback.filter(choice_name="3"))
async def chioce_three(call: CallbackQuery, callback_data: dict, statistics=3):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data}")

    await call.message.answer(f"Вы поставили этому кафе 3. Спасибо за ответ. Статистика этого кафе: {statistics}",
                              reply_markup=p_keyboard)


@dp.callback_query_handler(choice_callback.filter(choice_name="4"))
async def chioce_four(call: CallbackQuery, callback_data: dict, statistics=3):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data}")

    await call.message.answer(f"Вы поставили этому кафе 4. Спасибо за ответ. Статистика этого кафе: {statistics}",
                              reply_markup=p_keyboard)


@dp.callback_query_handler(choice_callback.filter(choice_name="5"))
async def chioce_five(call: CallbackQuery, callback_data: dict, statistics=3):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data}")

    await call.message.answer(f"Вы поставили этому кафе 5. Спасибо за ответ. Статистика этого кафе: {statistics}",
                              reply_markup=p_keyboard)


@dp.callback_query_handler(otsuv_callback.filter(otsuv_name="feedback"))
async def svoi_otsuv(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data}")
    await call.message.answer(f"Оставьте свой отзыв", reply_markup=choice)


@dp.callback_query_handler(otsuv_callback.filter(otsuv_name="chek"))
async def prosm_otsuv(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data}")
    await call.message.answer(f"Просмотр отзывов будет доступен позже.", db.get_review)
