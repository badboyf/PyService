#!/usr/bin/env python
# coding=utf-8

from flask import jsonify
from sqlalchemy import func

from db import connDB, close
import module
from module import User
from sqlalchemy_db import session
from util.util import RunException

def insert(user):
  conn = connDB()
  curs = conn.cursor()
  sql = 'insert into user(username, password) values (%s, %s)'
  param = (user.username, user.password)
  curs.execute(sql, param)
  close(curs, conn)

def get_all_user():
  conn = connDB()
  curs = conn.cursor()
  curs.execute('select * from user')
  result = curs.fetchall()

  titles = [desc[0] for desc in curs.description]
  
  res = []
  for row in result:
    s = dict()
    for title, val in zip(titles, row):
      s.setdefault(title, val)
    res.append(s)
  close(curs, conn)
  return jsonify(res)

def exist_user(username):
  conn = connDB()
  curs = conn.cursor()
  sql = 'select count(*) from user where user.username = "%s"' % (username)
  curs.execute(sql)
  result = curs.fetchone()
  close(curs, conn)
  if result[0] > 0:
    return True
  else :
    return False
  
def password_right(username=None, password=None):
  count = session.query(User).filter(User.username==username).filter(User.password==password).count()
  if count == 1:
    return True
  elif count == 0:
    return False
  else:
    raise RunException('count the same username and password more than one')
  
  
def get_user_by_username(username):
  conn = connDB()
  curs = conn.cursor()
  sql = 'select * from user where user.username = "%s";' % (username)
  curs.execute(sql)
  result = curs.fetchone()
  titles = [desc[0] for desc in curs.description]
  res = {}
  for title, val in zip(titles, result):
    res.setdefault(title, val)
  close(curs, conn)
  return jsonify(res)

def get_all():
  res_list = []
  for user in session.query(module.User).all():
    d = {}
    d.setdefault('id', user.id)
    d.setdefault('username', user.username)
    d.setdefault('password', user.password)
    res_list.append(d)
  session.close()
  return jsonify(res_list)

def get_user_by_name_psword(username=None, password=None):
  users = []
  for user in session.query(User).filter(User.username == username).filter(User.password == password).all():
    users.append(user)
  session.close()
  if len(users) == 1:
    return users[0]
  elif len(users) > 1:
    raise RunException('count user by username and password more than one')
  else:
    raise RunException('password is wrong')

def update(user):
  session.query(User).filter(User.id == user.id).update({'username':user.username, 'password':user.password})
  session.commit()
  session.close()
  
def get_user_by_id(user_id, check=True):
  user = session.query(User).filter(User.id == user_id).one_or_none()
  
  if user == None:
    if check:
      raise RunException('user not register')
  return user