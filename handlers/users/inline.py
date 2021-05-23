import logging

from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import choice_callback, otsuv_callback
from keyboards.inline.choice_buttons import p_keyboard, choice
from loader import dp, db


@dp.inline_handler(text="")
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="unknown",
                title="Введите название кафе для поиска",
                input_message_content=types.InputTextMessageContent(
                    message_text="Воспользуйтесь поиском, не нажимая на кнопку, пока не найдёте подходящее кафе"
                )
            )
        ]
    )


@dp.inline_handler()
async def some_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="unknown",
                title="Hard rock cafe",
                input_message_content=types.InputTextMessageContent(
                    message_text="Выберете необходиммый пункт"
                ),
                reply_markup=p_keyboard
            )
        ]
    )


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
    await call.message.answer(text=f"Оставьте свой отзыв", reply_markup=choice)


@dp.callback_query_handler(otsuv_callback.filter(otsuv_name="chek"))
async def prosm_otsuv(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data}")
    await call.message.answer(f"Отзывы:", db.get_review())
