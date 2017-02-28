#!/usr/bin/env python
#coding=utf-8
from util.util import date_formate
from response.default import ListResponse

class UserBlobsResponse(object):
  def __init__(self, blob):
    self.id = blob.id
    self.title = blob.title
    self.content = blob.content
    self.like = blob.like
    self.unlike = blob.unlike
    self.create_at = date_formate(blob.create_at)
    
class BlobDetailResponse(object):
  def __init__(self, blob):
    self.blob = UserBlobsResponse(blob).__dict__
    self.types = ListResponse()
  
class TypeResource(object):
  def __init__(self, blob_type):
    self.id=blob_type.id
    self.name=blob_type.name
    self.create_at=date_formate(blob_type.create_at)