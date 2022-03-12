# -*- coding: utf-8 -*-



import filters
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession



async def answer_on_hello(message: types.Message, db_session) -> None:

    await message.answer('hello too')

    session: AsyncSession
    async with db_session() as session:
        # Подключение к пулу бд (для возможной работы)
        pass



def register_messages(dp: Dispatcher) -> None:
    # Регистрация текст-хендлера (с фильром на кнопку) (работает без состояния)
    dp.register_message_handler(answer_on_hello, filters.CheckButton_hello(), content_types=['text'])
