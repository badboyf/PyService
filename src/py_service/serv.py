#!/usr/bin/evn python
# coding=utf-8
from flask import Flask
import json

from response.default import DefaultResponse 
from util_class import  RunException

from user import userF
from person_api import person_blue

app = Flask(__name__)

@app.errorhandler(RunException)
def run_exception(error):
  return json.dumps(DefaultResponse(success=False, data=error.msg).__dict__)

app.register_blueprint(userF, url_prefix='/user')
app.register_blueprint(person_blue, url_prefix='/person')

if __name__ == '__main__':
  app.run('0.0.0.0', 5000, debug=True)


