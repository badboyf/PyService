#!/usr/bin/env python
# coding=utf-8

class DefaultResponse(object):
  def __init__(self, data=None, success=True):
    self.data = data
    self.success = success

class ListResponse(list):
  def append(self, args):
    return list.append(self, args.__dict__)