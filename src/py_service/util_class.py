#!/usr/bin/env python

class RunException(RuntimeError):
  def __init__(self, msg):
    self.msg = msg

class UserC(object):
  def __init__(self, username=None, password=None):
    self.username = username
    self.password = password
    
date_return=lambda x : str(x) if x != None else None 