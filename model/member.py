# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean

from flask_app import db
from util.time import datetime_format


class Member(db.Model):
    __tablename__ = 'member'
    # 主键ID
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 用户名
    username = Column(String(length=255), unique=True)
    # 密码
    password = Column(String(length=255))
    # 邮箱
    email = Column(String(length=255), unique=True)

    # 是否启用true,false
    is_enable = Column(Boolean, default=True)
    # 是否删除
    is_delete = Column(Boolean, default=False)
    # 上次登录时间
    last_login_time = Column(DateTime)
    # 创建时间
    create_time = Column(DateTime, default=datetime.now)
    # 更新时间
    update_time = Column(DateTime, default=datetime.now)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'is_enable': self.is_enable,
            'is_delete': self.is_delete,
            'last_login_time': datetime_format(self.last_login_time) if self.last_login_time else "",
            'create_time': datetime_format(self.create_time) if self.create_time else "",
            'update_time': datetime_format(self.update_time) if self.update_time else "",

        }