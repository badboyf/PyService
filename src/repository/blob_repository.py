#!/usr/bin/python
# coding=utf-8
from module import Blob, Sort, Type
from sqlalchemy_db import session


def create(blob):
  session.add(blob)
  session.commit()
  blob_id = blob.id
  session.close()
  
  return blob_id

def get_blobs_by_user_id(user_id=None, type_id=None):
  sql = session.query(Blob).outerjoin(Sort, Blob.id==Sort.blob_id).filter(Blob.user_id==user_id)
  if not type_id == None:
    sql = sql.filter(Sort.type_id==type_id)
  
  result = []
  for blob in sql.group_by(Blob.id).all():
    result.append(blob)
  session.close()
  return result

def get_blob_detail(blob_id):
  result = []
  for blob, type in session.query(Blob, Type).filter(Blob.id==Sort.blob_id).filter(Type.id==Sort.type_id).all():
    result.append((blob, type))
  return result