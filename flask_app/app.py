# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import db_config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_config['url']
# app.config['SQLALCHEMY_BINDS'] = {
#     # 服务或数据库集中化导致的多数据库设计，需要拆分主数据库的业务表和油库配置表和台路表
#     # 'depot': depot_config['url'],
#     'gkfy': gkfy_config['url'],
#     'lroil': lroil_config['url'],
# }
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
