# -*- coding: utf-8 -*-


from sqlalchemy import Column, BigInteger
from models.db import Base



class Info_users(Base):
    # Таблица пользователя в базе данных
    __tablename__ = 'info_users'

    id_user = Column(BigInteger, primary_key=True)









