# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""
import json

from flask import request, make_response

from config import ex_time
import const


from flask_app import app
from model.member import Member

from util.common import build_ret, build_ret_one, get_g
from util.pjwt import validate_token

no_login_list = [
    '/',
    '/hello',
    '/member/signup',
    '/member/login',
    "/comment/tree",
]

@app.before_request
def prepare_request():
    """
    1.path check
    2.verify token
    3.add userinfo from token to g
    :return:
    """
    # todo: log here
    #request.params = get_request_args()

    #authorization()
    path = request.path
    if not path_check(path) and str(request.method) not in ['OPTIONS']:
        token = request.headers.get('token')
        success, result = validate_token(token=token)
        if success:
            init_member(result)
        else:
            # make_response(build_ret(result))
            return build_ret(result)



def authorization():

    path = request.path
    if not path_check(path) and str(request.method) not in ['OPTIONS']:
        token = request.headers.get('token')
        success, result = validate_token(token=token)
        if success:
            init_member(result)
        else:
            # make_response(build_ret(result))
            return build_ret(result)


def init_member(token_info):
    """
    初始化用户基本信息，包括（id, username, last_login）
    :param token_info:
    :return:
    """
    g = get_g()
    g.user = Member.query.filter(Member.id == token_info['id']).one()
    # id=token_info['id'], username=token_info['username'], last_login=token_info['last_login'])


def path_check(path):
    if path in no_login_list:
        return True
    else:
        return False


# def token_check(token):
#     success, result = validate_token(token)
#     if not success:
#         return False, make_response(build_ret(const.A_TIMEOUT))
#     return True, result

def get_request_args():
    args = {}
    if request.method == "GET":
        args = request.args.to_dict()
        # parse json
        for k, v in args.items():
            if args[k].startswith("{"):
                args[k] = json.loads(v)
    elif request.method == "POST":
        if not request.data and len(request.data):
            args = json.loads(request.data)
    return args