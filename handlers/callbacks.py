# -*- coding: utf-8 -*-


from aiogram import types, Dispatcher



async def callback_button_answer(call: types.CallbackQuery, db_session) -> None:
        
        await call.bot.send_message(chat_id=call.from_user.id, text='hello')
        



def register_callbacks(dp: Dispatcher):
        # Регистрация callback-хендлера (без фильтра) (работает со всеми состояниями)
        dp.register_callback_query_handler(callback_button_answer, state='*')
    