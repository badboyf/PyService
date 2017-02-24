#!/usr/bin/env python
# coding=utf-8
from flask import request
from flask import render_template
from flask import make_response
import json

from serv import app
# app.debug = True
# app.config.update(
#   DEBUG=True
#   SECRET_KEY='value'                
# )
# app.config.from_object('yourapplication.default_settings_OR_class')
# app.config.from_envvar('YOURAPPLICATION_SETTINGS')


# @app.errorhandler(404)
# def page_notfound(error):
#   return render_template('not_found.html'), 404
class RunException(RuntimeError):
  def __init__(self, msg, code):
    self.msg = msg
    self.code = code


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('not_found.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

@app.errorhandler(RunException)
def exce(error):
  return 'ERROR[msg: %s, code: %d]' % (error.msg, error.code), error.code

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return "GET index page"
  elif request.method == 'POST':
    return "POST index"
  
@app.route('/hello')
@app.route('/hello/<name>')
def greeting(name=None):
  return render_template('hello.html', name=name)

@app.route('/user/<username>', methods=['GET', 'POST'])
def get_name(username):
  if request.method == 'GET':
    return "user: %s by GET" % username
  elif request.method == 'POST':
    return "store user: %s by POST" % username

@app.route('/user/<int:user_id>')
def get_id(user_id):
  return "id: %d" % user_id

@app.route('/login', methods=['POST'])
def login():
  return json.loads(request.data)['username']
  
@app.route('/search', methods=['GET'])
def search():
  word = request.args.get('key', '')
  return 'key word is: %s' % word

@app.route('/exce', methods=['GET'])
def test_e():
  raise RunException('occur', 100000)
  return 'no error'
