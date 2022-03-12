# -*- coding: utf-8 -*-


from aiogram import types


class UserKeyboards:

    list_main_menu_button_text = [
        'hello',
        ]
    main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for text in list_main_menu_button_text:
        main_menu.add(text)

