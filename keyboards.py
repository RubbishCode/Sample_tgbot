# -*- coding: utf-8 -*-


from aiogram import types


class Keyboard:
    list_text_button: list
    keyboard: types.ReplyKeyboardMarkup


class UserKeyboards:

    async def main_menu() -> Keyboard:
        list_text_button = [
            'hello',
            ]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for text in list_text_button:
            keyboard.add(text)

        return type('Keyboard', (), {
            'list_text_button': list_text_button,
            'keyboard': keyboard,
        })

