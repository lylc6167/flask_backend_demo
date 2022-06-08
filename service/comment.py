# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""

from datetime import datetime, timedelta
from random import random

import const
from flask_app import db
# from schema.atm import OrderSchema
# from schema.lroil import AutotableSchema
from model.comment import Comment
from model.member import Member

from util.time import str_to_date, datetime_format


# 添加评论
def add(member_id: int, content: str, parent_id: int = None) -> (bool, dict):
    parent_comment = Comment.query.filter(
        Comment.id == parent_id
    ).one_or_none()
    if parent_id and not parent_comment:
        return False, const.COMMENT_PARENT_ID_NOT_FOUND

    member = Member.query.filter(Member.id == member_id).one_or_none()
    if not member:
        return False, const.MEMBER_ID_NOT_FOUND

    comment = Comment(
        member_id=member_id,
        username=member.username,
        parent_id=parent_id,
        content=content
    )
    db.session.add(comment)
    db.session.flush()

    comment.path = parent_comment.path + [comment.id] if parent_id else [comment.id]
    comment.level = len(comment.path)

    db.session.commit()
    data = {'comment_id': comment.id}
    return True, data


# 展示评论树
def tree(comment_id: int=None) -> (bool, list):
    if comment_id:
        exist_root = Comment.query.filter(Comment.id == comment_id).one_or_none()
        if not exist_root:
            return False, const.COMMENT_ID_NOT_FOUND

        comments = Comment.query.filter(
            Comment.path.contains([comment_id])
        ).order_by(
            Comment.level,
            Comment.create_time  # .desc()翻转之后不需要倒叙时间
        ).all()

        result = generate_tree(comments, comments[0].parent_id)
    else:
        comments = Comment.query.order_by(
            Comment.level,
            Comment.create_time  # .desc()翻转之后不需要倒叙时间
        ).all()
        root_comment = Comment(id=-1, parent_id=-2, member_id=None, content='')

        result = generate_tree([root_comment] + comments, -2)[0]['children']

    return True, result


# 树生成器
def generate_tree(comment_list: list, parent_id: int) -> list:
    result = []
    for c in comment_list[::-1]:  # 倒序遍历

        node = {
            'id': c.id,
            'parent_id': c.parent_id,
            'member_id': c.member_id,
            'member_name': c.username,
            'content': c.content,
            'create_time': datetime_format(c.create_time) if c.create_time else "",
            'children': []
        }

        if node['parent_id']==parent_id:
            node['children'] = generate_tree(comment_list[1:], node['id'])  # 去掉已计算数据
            result.append(node)
    return result
