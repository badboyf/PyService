#!/usr/bin/env python
import json
from response.default import DefaultResponse

class RunException(RuntimeError):
  def __init__(self, msg):
    self.msg = msg

class UserC(object):
  def __init__(self, username=None, password=None):
    self.username = username
    self.password = password
    
date_formate=lambda x : str(x) if x != None else None 

res = lambda data, success=True : json.dumps(DefaultResponse(data=data, success=success).__dict__)