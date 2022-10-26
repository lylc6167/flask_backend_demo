# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean  # , ARRAY
from sqlalchemy.dialects.postgresql import ARRAY

from flask_app import db
from util.time import datetime_format


class Comment(db.Model):
    __tablename__ = 'comment'
    # 主键ID
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 用户id
    member_id = Column(Integer)
    # 用户名
    username = Column(String(length=255))
    # 内容
    content = Column(String(length=300))
    # 创建时间
    create_time = Column(DateTime, default=datetime.now)
    # 上级id
    parent_id = Column(Integer, default=-1)
    # 全路径，从根节点到当前节点的边
    path = Column(ARRAY(Integer))
    # 层级
    level = Column(Integer)
    # 是否启用true,false
    is_enable = Column(Boolean, default=True)
    # 是否删除
    is_delete = Column(Boolean, default=False)

    def to_json(self):
        return {
            'id': self.id,
            'member_id': self.member_id,
            'content': self.content,
            'create_time': datetime_format(self.create_time) if self.create_time else "",
            'parent_id': self.parent_id,
            'path': self.path,
            'level': self.level,
            'is_enable': self.is_enable,
            'is_delete': self.is_delete,
        }
