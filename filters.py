# -*- coding: utf-8 -*-


from aiogram.dispatcher.filters import Filter
from aiogram import types
from keyboards import UserKeyboards



class CheckButton_hello(Filter):
   # Фильтр для проверки текста кнопки
   async def check(self, message: types.Message) -> bool:
      keyboard = await UserKeyboards.main_menu()
      return message.text == keyboard.list_text_button[0]
