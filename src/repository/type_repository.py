#!/usr/bin/python
#coding=utf-8
from module import Type
from sqlalchemy_db import session
from util.util import RunException

def get_type_by_id(type_id=0,user_id=0 , check=True):
  result = session.query(Type).filter(Type.id==type_id).filter(Type.user_id==user_id).one_or_none()
  if result == None:
    if check:
      raise RunException('result not exist')
  
  return result