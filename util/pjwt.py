# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""
import random
import string
import time
from datetime import datetime

import jwt

import const
from config import ex_time, jwt_conf


def en_token(id: int, username: str, last_login: str, remember: bool=False) -> str:
    """
    :param id: int
    :param username: str
    :param remember:  bool  #默认False为一天到期token
    :return:
    """
    iat = time.time()
    # exp = iat + ex_time['token_long_ex']
    payload = {
        'id': str(id),
        'username': str(username),
        'last_login': str(last_login),
        'iat': iat,
        'exp': iat + ex_time['token_long_ex'] if remember else iat + ex_time['token_short_ex']

    }
    # if flag:
    #     payload['flag'] = 0  # 默认一次性token
    #     payload['exp'] = iat + ex_time['token_short_ex']
    # else:
    #     payload['flag'] = 1
    #     payload['exp'] = iat + ex_time['token_long_ex']

    token = jwt.encode(
        payload, jwt_conf['token_key'], algorithm='HS256')
    return token


def validate_token(token) -> (bool, dict):
    if token is None:
        return False, const.NO_TOKEN_ERROR
    token = str(token)

    token_keys = jwt_conf['token_key']
    # payload = None
    # msg = None

    try:
        payload = jwt.decode(token, token_keys, algorithms=['HS256'])
        # jwt有效、合法性校验
    except jwt.ExpiredSignatureError:
        return False, const.TOKEN_EXP_ERROR
    except jwt.DecodeError:
        return False, const.TOKEN_DECODE_ERROR
    except jwt.InvalidTokenError:
        return False, const.TOKEN_INVALID_ERROR
    return True, payload

