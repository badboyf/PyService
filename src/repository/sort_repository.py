#!/usr/bin/python
#coding=utf-8
from module import Sort
from sqlalchemy_db import session
from util.util import RunException

def create(sort):
  session.add(sort)
  session.commit()
  session.close()