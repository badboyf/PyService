#!/usr/bin/env python
#coding=utf-8

class PersonResponse(object):
  def __init__(self, person):
    self.user_id = person.user_id
    self.name = person.name
    self.address = person.address
    self.gender = person.gender
    self.id = person.id
    self.create_at = person.create_at
    self.update_at = person.update_at