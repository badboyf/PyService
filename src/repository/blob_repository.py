#!/usr/bin/python
# coding=utf-8
from module import Blob
from sqlalchemy_db import session


def create(blob):
  session.add(blob)
  session.commit()
  blob_id = blob.id
  session.close()
  
  return blob_id
