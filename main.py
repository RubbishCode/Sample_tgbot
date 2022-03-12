# -*- coding: utf-8 -*-



import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

import config
from handlers.callbacks import register_callbacks
from handlers.commands import register_commands
from handlers.messages import register_messages
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from middleware import Middleware
from models.db import Base
import filters



async def while_pass(bot: Bot) -> None:

    # Возможный цикл для тайминговых действий (ежеминутных в данном случае)
    db_session = bot['db']
    session: AsyncSession
    async with db_session() as session:
        # Подключение к пулу бд
        pass



async def main():

    storage = RedisStorage(
        host=config.Redis.host, 
        port=config.Redis.port, 
        db=config.Redis.db)


    engine = create_async_engine(
        config.DataBase.postgres_url,
        future=True
    )
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


    async_sessionmaker = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )

    bot = Bot(token=config.Bot.token, parse_mode="HTML")
    bot["db"] = async_sessionmaker
    dp = Dispatcher(bot, storage=storage)


    register_commands(dp)
    register_messages(dp)
    register_callbacks(dp)


    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        while_pass, 'interval', [bot], seconds=60,
        )
    scheduler.start()


    try:
        dp.bind_filter(filters.CheckButton_hello)

        dp.middleware.setup(Middleware())
        await dp.start_polling()
        
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()
    



if __name__ == '__main__':
    asyncio.run(main())

  
