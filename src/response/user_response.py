#!/usr/bin/env python
# coding=utf-8

class LoginResponse(object):
  def __init__(self):
    self.user_id = None
    self.uername = None
    self.name = None
    self.address = None
    self.gender = None
    self.person_id = None
  
  def init(self, user=None, person=None):
    if user:
      self.user_id = user.id
      self.uername = user.username
      if not person:
        self.person_id = person.id
        self.name = person.name
        self.address = person.address
        self.gender = person.gender
    return self.__dict__
