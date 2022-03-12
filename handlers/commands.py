# -*- coding: utf-8 -*-


from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from keyboards import UserKeyboards
from models.users import Info_users
from sqlalchemy.ext.asyncio import AsyncSession



async def start(message: types.Message, state: FSMContext, db_session) -> None:

    await state.finish()

    session: AsyncSession
    async with db_session() as session:
        await session.merge(Info_users(id_user=message.from_user.id))
        await session.commit()
        

    await message.answer('hello', reply_markup=UserKeyboards.main_menu)





def register_commands(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands='start', state='*')
