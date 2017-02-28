#!/usr/bin/env python
# coding=utf-8
import datetime

class WriteBlobRequest(object):
  def __init__(self, **args):
    self.user_id = args.get("user_id")
    self.title = args.get("title")
    self.content = args.get("content")
    self.like = 0
    self.unlike = 0
    self.create_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    self.update_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    self.type_id = args.get("type_id")