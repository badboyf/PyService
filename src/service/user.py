#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint
from user_repository import *
from flask import request
import json

from util_class import UserC
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
  print '*' * 100
  username = json.loads(request.data).get('username')
  password = json.loads(request.data).get('password')
  print UserC(username, password)
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