#!/usr/bin/env python
# coding=utf-8

from sqlalchemy import Table, Column, Integer, String, Date, Float, create_engine  
from sqlalchemy.orm import sessionmaker

DB_URI = r'mysql://root:root@192.168.1.109:3306/fzk'
def get_DB():
  db = create_engine(DB_URI)
  return db

def get_Session():
  Session = sessionmaker(bind=get_DB())
  session = Session()
  return session

session = get_Session()