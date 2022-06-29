# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""
from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop

from config import web
from flask_app import app


s = HTTPServer(WSGIContainer(app))
s.listen(web['port']) # 监听 8080 端口
#s.listen(8081)
#s.listen(8082)
IOLoop.current().start()

