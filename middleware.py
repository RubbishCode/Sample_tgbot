# -*- coding: utf-8 -*-


from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware



class Middleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        data['db_session'] = message.bot.get("db")
        

    async def on_process_callback_query(self, call: types.CallbackQuery, data: dict):
        data['db_session'] = call.bot.get("db")
