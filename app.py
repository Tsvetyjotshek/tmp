from handlers.users.help import bot_help
from loader import bot
from utils.notify_admins import on_startup_notify


async def helping(dp):
    await bot_help(dp)


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)


async def on_shutdown():
    await bot.close()


if __name__ == '__main__':
    from aiogram import executor
    from loader import dp

    executor.start_polling(dp, on_startup=on_startup)
