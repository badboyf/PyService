# /usr/bin/env python
# coding=utf-8

from flask import Blueprint
from flask import request

import time
import datetime
import json

import person_repository
import user_repository
from response.person_response import PersonResponse
from response.default import DefaultResponse
from util_class import RunException, date_return
from module import Person

person_blue = Blueprint('person', __name__)

@person_blue.route('/<int:user_id>', methods=['GET', 'POST', 'PUT'])
def get_person_by_user_id(user_id):
  if request.method == 'GET':
    
    person_repository.get_person_info_by_user_id(user_id)
    
    person = PersonResponse(person_repository.get_person_by_user_id(user_id))
    person.create_at = date_return(person.create_at)
    person.update_at = date_return(person.update_at)
    return json.dumps(DefaultResponse(data=person.__dict__).__dict__)
  elif request.method == 'POST' or request.method == 'PUT':
    user_repository.get_user_by_id(user_id, check=True)

    data_req = json.loads(request.data)
    
    if not person_repository.get_person_by_user_id(user_id, check=False):
#       person_repository.insert_one_person(Person(user_id=user_id,name=name, address=address, gender=gender))
      data_req['user_id'] = user_id
      person_repository.insert_one_person(Person(**data_req))
      return json.dumps(DefaultResponse(data='create success').__dict__)
    else:
      data_req['update_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      person_repository.update(user_id, data_req)
      return json.dumps(DefaultResponse(data='update success').__dict__)
