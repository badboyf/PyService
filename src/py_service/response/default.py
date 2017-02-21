#!/usr/bin/env python
# coding=utf-8

class DefaultResponse(object):
  def __init__(self, data=None, success=True):
    self.data = data
    self.success = success
