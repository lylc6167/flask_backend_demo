# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""
import time
import json

from flask import request
from marshmallow import ValidationError

from flask_app import app
from util.common import build_ret, build_ret_one, tran_bool
import const

from schema.member import MemberSingupSchema, MemberLoginSchema
from service import member


# 注册
@app.route('/member/signup', methods=['POST'])
def member_signup():
    args = request.get_json()

    try:
        errors = MemberSingupSchema().validate(args, partial=False)
        if errors and len(errors):
            return build_ret_one(const.CODE_VALIDATE_ERROR, data={'sub_error': json.dumps(errors)})
    except ValidationError as err:
        sub_error = err.messages
        return build_ret_one(const.CODE_VALIDATE_ERROR, data={'sub_error': sub_error})

    username = str(args.get('username'))
    password = str(args.get('password'))
    email = str(args.get('email'))

    success, result = member.signup(
        username=username,
        password=password,
        email=email
    )
    if not success:
        return build_ret_one(code=result)
    else:
        return build_ret(const.SYS_SUCCESS)



# 登录
@app.route('/member/login', methods=['POST'])
def member_login():
    args = request.get_json()

    try:
        errors = MemberLoginSchema().validate(args, partial=False)
        if errors and len(errors):
            return build_ret_one(const.CODE_VALIDATE_ERROR, data={'sub_error': json.dumps(errors)})
    except ValidationError as err:
        sub_error = err.messages
        return build_ret_one(const.CODE_VALIDATE_ERROR, data={'sub_error': sub_error})

    username = str(args.get('username'))
    password = str(args.get('password'))
    remember_me = tran_bool(args.get('remember_me')) if args.get('remember_me') else None

    success, result = member.login(
        username=username,
        password=password,
        remember_me=remember_me
    )
    if not success:
        return build_ret_one(code=result)
    else:
        return build_ret(const.SYS_SUCCESS, data=result)

# 退出
@app.route('/member/singout', methods=['POST'])
def signout():
    pass