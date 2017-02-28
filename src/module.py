# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, Text, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Blob(Base):
    __tablename__ = 'blob'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    title = Column(Text)
    content = Column(Text)
    like = Column(Integer, nullable=False, server_default=text("'0'"))
    unlike = Column(Integer, nullable=False, server_default=text("'0'"))
    create_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_at = Column(DateTime)


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    name = Column(String(45))
    address = Column(String(45))
    gender = Column(String(45))
    create_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    update_at = Column(DateTime)


class Sort(Base):
    __tablename__ = 'sort'

    id = Column(Integer, primary_key=True)
    blob_id = Column(Integer, nullable=False)
    type_id = Column(Integer)
    create_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))


class Type(Base):
    __tablename__ = 'type'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    name = Column(String(45), nullable=False)
    create_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_at = Column(DateTime)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(45))
    password = Column(String(45))
    create_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    update_at = Column(DateTime)
