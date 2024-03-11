import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
import logging
from random_fox.handlers import career_choice


async def main():
    # Включаем логгирование
    logging.basicConfig(level=logging.INFO)

    # Создаем объект бота
    # Нужно будет создать у себя файл config.py (на уровне main.py)
    # и создать там переменную с названием config
    bot = Bot(token=config.token)

    # Диспечер
    dp = Dispatcher()

    dp.include_router(career_choice.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
