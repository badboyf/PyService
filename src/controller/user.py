#!/usr/bin/env python
# coding=utf-8
from flask import Blueprint, jsonify
from repository.user_repository import get_user_by_username, exist_user, insert, get_user_by_name_psword, update, get_all
from repository.person_repository import get_person_by_user_id
from flask import request
from request.user_request import LoginRequest
from response.user_response import LoginResponse
from service.user_service import *
import json

from util.util import UserC
from response.default import  DefaultResponse

userF = Blueprint('user', __name__)

@userF.route('/', methods=['GET'])
def getUser():
  return get_all()

@userF.route('/<username>', methods=['GET'])
def getUserInfo(username):
  return get_user_by_username(username)

@userF.route('/', methods=['POST'])
def register():
  username = json.loads(request.data).get('username')
  password = json.loads(request.data).get('password')
  if exist_user(username):
    return 'user already exist'
  else:
    user = UserC(username, password)
    insert(user)
    return 'register success'
  
@userF.route('/password', methods=['PUT'])
def change_password():
  data = json.loads(request.data)
  username = data.get('username')
  password = data.get('password')
  new_password = data.get('new_password')
  if not exist_user(username):
    return json.dumps(DefaultResponse(success=False, data='user not exist').__dict__)
  user = get_user_by_name_psword(username, password)
  user.password = new_password
  update(user)
  return json.dumps(DefaultResponse(data='update success').__dict__)

@userF.route('/login', methods=['PUT'])
def login():
  req = LoginRequest(**(json.loads(request.data)))
  if exist_user(req.username):
    user = get_user_by_name_psword(req.username, req.password)
    person = get_person_by_user_id(user.id, check=False)
    return json.dumps(DefaultResponse(data=LoginResponse().init(user, person)).__dict__)
  else:
    return json.dumps(DefaultResponse(data='user not exist', success=False).__dict__)





