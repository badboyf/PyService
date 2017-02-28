#!/usr/bin/env python
# coding=utf-8

from sqlalchemy import Table, Column, Integer, String, Date, Float, create_engine  
from sqlalchemy.orm import sessionmaker
from config import db_ip,db_port, db_name, db_pswd, db_schema 

DB_URI = 'mysql://%s:%s@%s:%d/%s' % (db_name, db_pswd, db_ip, db_port, db_schema)
def get_DB():
  db = create_engine(DB_URI)
  return db

def get_Session():
  Session = sessionmaker(bind=get_DB())
  session = Session()
  return session

session = get_Session()