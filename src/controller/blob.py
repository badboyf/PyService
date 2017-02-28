# /usr/bin/python
# coding=utf-8

from flask import Blueprint, request
import json

from repository import blob_repository, type_repository, sort_repository
from request.blob_request import WriteBlobRequest
from module import Blob, Sort
from util.util import res

blob_blue = Blueprint('blob', __name__)

@blob_blue.route('/write', methods=['POST'])
def write():
  req = WriteBlobRequest(**json.loads(request.data))
  type_id = type_repository.get_type_by_id(type_id=req.type_id, user_id=req.user_id, check=True).id
  
  
  blob = Blob(user_id=req.user_id, title=req.title, content=req.content, update_at=req.update_at)
  blob_id = blob_repository.create(blob)
  
  sort = Sort(blob_id=blob_id, type_id=type_id)
  sort_repository.create(sort)
  return res(data='create success')
