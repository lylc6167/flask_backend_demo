# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""
from flask import request

import const
from flask_app import app
from service import comment
from util.common import build_ret, build_ret_one, get_g


# 添加评论
@app.route('/comment/add', methods=['POST'])
def add_comment():
    args = request.get_json()
    current_user = get_g().user

    # member_id = int(args.get('member_id'))
    content = str(args.get('content'))
    parent_id = int(args.get('parent_id')) if args.get('parent_id') else None

    success, result = comment.add(
        member_id=current_user.id,
        content=content,
        parent_id=parent_id,
    )
    if not success:
        return build_ret_one(code=result)
    else:
        return build_ret(const.SYS_SUCCESS, data=result)


# 获取评论树
@app.route('/comment/tree', methods=['GET'])
def tree_comment():
    # args = request.get_json()  #post
    args = request.args.to_dict()
    
    comment_id = int(args.get('comment_id')) if args.get('comment_id') else None

    success, result = comment.tree(comment_id=comment_id)
    if not success:
        return build_ret_one(code=result)
    else:
        return build_ret(const.SYS_SUCCESS, data=result)