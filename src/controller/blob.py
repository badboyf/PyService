# /usr/bin/python
# coding=utf-8
from flask import Blueprint, request, jsonify
import json

from repository import blob_repository, type_repository, sort_repository, user_repository
from request.blob_request import WriteBlobRequest
from module import Blob, Sort
from util.util import res
from response.blob_response import UserBlobsResponse, BlobDetailResponse, TypeResource

from response.default import DefaultResponse, ListResponse

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

@blob_blue.route('/user/<int:user_id>', methods=['GET'])
def getUserBlobs(user_id):
  type_id = request.args.get('type_id', None)
  user_repository.get_user_by_id(user_id, check=True)
  response = ListResponse()
  for blob in blob_repository.get_blobs_by_user_id(user_id, type_id):
    response.append(UserBlobsResponse(blob))
  return res(data=response)

@blob_blue.route('/blob_id/<int:blob_id>')
def getBlobDetail(blob_id):
  d = dict()
  for blob, blob_type in blob_repository.get_blob_detail(blob_id):
    detail = d.get(blob.id)
    if detail == None:
      detail = BlobDetailResponse(blob)
    types = detail.types
    types.append(TypeResource(blob_type))
    d.setdefault(blob.id, detail)
  
  response = ListResponse()
  for key in d.keys():
    response.append(d.get(key))
  
  return res(data=response)

