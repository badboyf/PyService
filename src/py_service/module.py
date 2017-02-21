# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    name = Column(String(45))
    address = Column(String(45))
    gender = Column(String(45))
    create_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    update_at = Column(DateTime)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(45))
    password = Column(String(45))
    create_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    update_at = Column(DateTime)