#!/usr/bin/env python
# coding=utf-8

class LoginRequest(object):
  def __init__(self, **args):
    self.username = args.get("username")
    self.password = args.get("password")
