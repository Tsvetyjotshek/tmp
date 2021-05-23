from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.config import URL_menu

# choice = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="1",
#                                  callback_data="choice:1"),
#         ],
#         [
#             InlineKeyboardButton(text="2",
#                                  callback_data="choice:2"),
#         ],
#         [
#             InlineKeyboardButton(text="3",
#                                  callback_data="choice:3"),
#         ],
#         [
#             InlineKeyboardButton(text="4",
#                                  callback_data="choice:4"),
#         ],
#         [
#             InlineKeyboardButton(text="5",
#                                  callback_data="choice:5"),
#         ],
#
#     ]
# )

choice = InlineKeyboardMarkup(row_width=5)

choice1 = InlineKeyboardButton(text="1", callback_data="choice:1:3")
choice.insert(choice1)

choice2 = InlineKeyboardButton(text="2", callback_data="choice:2:3")
choice.insert(choice2)

choice3 = InlineKeyboardButton(text="3", callback_data="choice:3:3")
choice.insert(choice3)

choice4 = InlineKeyboardButton(text="4", callback_data="choice:4:3")
choice.insert(choice4)

choice5 = InlineKeyboardButton(text="5", callback_data="choice:5:3")
choice.insert(choice5)

p_keyboard = InlineKeyboardMarkup(row_width=3)

menu = InlineKeyboardButton(text="Меню", url=URL_menu)
p_keyboard.insert(menu)

otsuv = InlineKeyboardButton(text="Оставить отзыв", callback_data="otsuv:feedback")
p_keyboard.insert(otsuv)

chek = InlineKeyboardButton(text="Посмотреть отзывы", callback_data="otsuv:chek")
p_keyboard.insert(chek)

# p_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Меню", url=URL_menu),
#         ],
#         [
#             InlineKeyboardButton(text="Оставить отзыв", reply_markup=choice),
#         ],
#         [
#             InlineKeyboardButton(text="Посмотреть отзывы"),
#         ],
#     ]
# )
