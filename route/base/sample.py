# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""
from flask_app import app
import time


@app.route('/', methods=['GET'])
def hello1():
    return 'hello world first time!!!!!'

@app.route('/hello', methods=['GET'])
def hello2():
    return 'hello world second time!!!!!'