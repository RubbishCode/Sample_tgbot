# -*- coding: utf-8 -*-


from aiogram.dispatcher.filters.state import State, StatesGroup



class Test(StatesGroup):
    # Машинное состояние пользователя 
    text = State()


