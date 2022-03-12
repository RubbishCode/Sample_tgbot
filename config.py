# -*- coding: utf-8 -*-


class Bot:
    token = ''


class DataBase:
    # Данные для подключения к бд psql
    host = 'localhost'
    name = ''
    user = 'postgres'
    password = ''

    postgres_url = f"postgresql+asyncpg://{user}:{password}@{host}/{name}"


class Redis:
    # Данные для подключения к бд redis
    host = 'localhost'
    port = 6379
    db = 7


class ChatID:
    admins = []


