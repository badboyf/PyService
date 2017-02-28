#!/usr/bin/env python
# coding=utf-8
from config import db_ip, db_port, db_name, db_pswd, db_schema 
import MySQLdb as db

def connDB():
#   conn = mdb.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='fzk', charset='utf8')
  config = {
    'host': db_ip,
    'port': db_port,
    'user': db_name,
    'passwd': db_pswd,
    'db': db_schema,
    'charset': 'utf8'
  }
  conn = db.connect(**config)
  conn.autocommit(1)
  return conn

def close(curs, conn):
  curs.close()
  conn.close()
  
