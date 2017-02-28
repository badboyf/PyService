#!/usr/bin/env python
# coding=utf-8
from util.util import date_formate
from response.default import ListResponse

class UserBlobsResponse(dict):
  def __init__(self, blob):
    self.setdefault('id', blob.id)
    self.setdefault('title', blob.title)
    self.setdefault('content', blob.content)
    self.setdefault('like', blob.like)
    self.setdefault('unlike', blob.unlike)
    self.setdefault('create_at', date_formate(blob.create_at))
    
class BlobDetailResponse(dict):
  def __init__(self, blob):
    self.setdefault('blob', UserBlobsResponse(blob))
    self.setdefault('types', [])
  
class TypeResource(dict):
  def __init__(self, blob_type):
    self.setdefault('id', blob_type.id)
    self.setdefault('name', blob_type.name)
    self.setdefault('create_at', date_formate(blob_type.create_at))
