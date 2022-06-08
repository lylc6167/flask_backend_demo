# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""
# from datetime import datetime
#
# from sqlalchemy import Column, Integer, String, DateTime, Boolean
#
# from flask_app import db
#
#
# class User(db.Model):
#     __tablename__ = 'user'
#     # 主键ID
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     # 用户名
#     username = Column(String(length=255))
#     # 密码
#     password = Column(String(length=255))
#     # 邮箱
#     email = Column(String(length=255))
#
#     # 是否启用true,false
#     is_enable = Column(Boolean, default=True)
#     # 是否删除
#     is_delete = Column(Boolean, default=False)
#     # 上次登录时间
#     last_login_time = Column(DateTime)
#     # 创建时间
#     create_time = Column(DateTime, default=datetime.now)
#     # 更新时间
#     update_time = Column(DateTime, default=datetime.now)
