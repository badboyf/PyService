#!/usr/bin/env python
# coding=utf-8

from module import Person, User
from sqlalchemy_db import session
from util_class import RunException

def get_person_by_user_id(user_id, check=True):
  persons = []
  for person in session.query(Person).filter(Person.user_id == user_id).all():
    persons.append(person)
  if len(persons) == 0:
    if check:
      raise RunException(msg='person not found by user_id is [%d]' % (user_id))
    else:
      return None
  elif len(persons) > 1:
    raise RunException(msg='person more than one by user_id is [%d]' % (user_id))
  else:
    return persons[0]

def insert_one_person(person):
  session.add(person)
  session.commit()
  session.close()
  
def update(user_id, person):
  session.query(Person).filter(Person.user_id == user_id).update(person)
  session.commit()
  session.close()
  
def get_person_info_by_user_id(user_id):
  persons = []
  for user, person in session.query(User, Person).join(Person, Person.user_id==User.id).filter(User.id==user_id).all():
    print user.id, person.id
