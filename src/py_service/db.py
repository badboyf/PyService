#!/usr/bin/env python
# coding=utf-8

import MySQLdb as db

def connDB():
#   conn = mdb.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test', charset='utf8')
  config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    'db': 'fzk',
    'charset': 'utf8'
  }
  conn = db.connect(**config)
  conn.autocommit(1)
  return conn

def close(curs, conn):
  curs.close()
  conn.close()
  
