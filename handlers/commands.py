# -*- coding: utf-8 -*-


from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from keyboards import UserKeyboards
from models.users import Info_users
from sqlalchemy.ext.asyncio import AsyncSession



async def start(message: types.Message, state: FSMContext, db_session) -> None:

    # Завершение (бывшего возможого) состояния
    await state.finish()

    session: AsyncSession
    async with db_session() as session:
        # Добавление пользователя в бд
        await session.merge(Info_users(id_user=message.from_user.id))
        await session.commit()
        
    keyboard = await UserKeyboards.main_menu()
    await message.answer('hello', reply_markup=keyboard.keyboard)





def register_commands(dp: Dispatcher) -> None:
    # Регистрация команд-хендлера комманды старт (без фильров) (работает со всеми состояниями)
    dp.register_message_handler(start, commands='start', state='*')
