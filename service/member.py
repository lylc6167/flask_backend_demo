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
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash


from model.member import Member
from schema.member import MemberSingupSchema, MemberLoginSchema

from util.time import str_to_date, datetime_format
from util.pjwt import en_token


# 注册
def signup(username: str, password: str, email: str) -> (bool, dict):
    """
    :param username:
    :param password:
    :param email:
    :return:
    """
    exist_username_or_email = Member.query.filter(
        or_(Member.username == username, Member.email == email)
    ).all()
    if exist_username_or_email:
        return False, const.MEMBER_OR_EMAIL_EXIST

    args = {
        'username': username,
        'password': generate_password_hash(password),  # 后端加密
        'email': email
    }

    member = MemberSingupSchema().load(args)

    db.session.add(member)
    db.session.commit()

    return True, const.SYS_SUCCESS


# 登录
def login(username: str, password: str, remember_me: bool=False) -> (bool, dict):
    """
    check_password_hash(hash, password)
    :param username:
    :param password:
    :param remember_me:
    :return:
    """
    member = Member.query.filter(
        Member.username == username
    ).one_or_none()

    if not member:
        return False, const.MEMBER_USERNAME_NOT_FOUND

    correct_password = check_password_hash(member.password, password)
    if not correct_password:
        return False, const.MEMBER_LOGIN_PASSWORD_WRONG

    member.last_login_time = datetime.now()

    db.session.add(member)
    db.session.commit()

    token = en_token(id=member.id, username=username, last_login=datetime_format(member.last_login_time), remember=remember_me)

    data = {
        'token': token
    }

    return True, data




# 退出
def logout():
    pass








