"""
flask run 启动服务后再进行接口测试
"""
import json

import requests

import const


HEADERS = {"Content-Type": "application/json"}
url = 'http://127.0.0.1:5000'

api_signup = '/member/signup'
api_login = '/member/login'

api_comment_add = '/comment/add'
api_comment_tree = '/comment/tree'

data_signup = {
    'username': '6167Test',
    'password': '6167P@ssw0rd',
    'email': '6167@test.com'
}

data_login = {
    'username': '6167Test',
    'password': '6167P@ssw0rd',    # '123456'md5加密一次
    # 'remember_me': 'true'
}

data_comment_add = {'content': 'hello world'}

data_comment_tree = {'comment_id': 1}

def get_token(login_data):
    login_r = requests.post(url + api_login,
                            json.dumps(login_data),
                            headers=HEADERS)
    NEW_HEADERS, NEW_HEADERS['token'] = HEADERS, json.loads(login_r.text)['data']['token']
    return NEW_HEADERS


def post(api, data, headers):
    # data['token'] = __token
    respon = requests.post(url + api,
                           json.dumps(data),
                           headers=headers)  # get_token(login_data))
    return json.loads(respon.text) \
        if respon.status_code == 200 \
        else respon.status_code


def get(api, data, headers):
    respon = requests.get(url + api,
                          params=data,  # {'a':123}
                          headers=headers)
    return json.loads(respon.text) \
        if respon.status_code == 200 \
        else respon.status_code


def test_whole_process():
    """
    测试顺序
    1./comment/tree get
    2./comment/add post
    3./member/signup post
    4./member/login post
    6./comment/add.....  post
    7./comment/tree get
    """
    # 获取所有评论
    res_data = get('/comment/tree', {}, headers=HEADERS)
    assert res_data['code'] == const.SYS_SUCCESS.code

    # 添加评论
    res_data = post('/comment/add', {'content': 'hello world'}, headers=HEADERS)
    assert res_data['code'] == const.NO_TOKEN_ERROR.code

    # 注册
    res_data = post('/member/signup', {
        'username': '6167Test',
        'password': '6167P@ssw0rd',
        'email': '6167@test.com'
    }, headers=HEADERS)
    assert res_data['code'] == const.SYS_SUCCESS.code

    # 相同邮箱二次注册
    res_data = post('/member/signup', {
        'username': '6167Test2',
        'password': '6167P@ssw0rd',
        'email': '6167@test.com'
    }, headers=HEADERS)
    assert res_data['code'] == const.MEMBER_OR_EMAIL_EXIST.code

    # 登录
    res_data = post('/member/login', {
        'username': '6167Test',
        'password': '6167P@ssw0rd',
        'remember_me': 'true'
    }, headers=HEADERS)
    assert res_data['code'] == const.SYS_SUCCESS.code

    NEW_HEADERS = get_token({
        'username': '6167Test',
        'password': '6167P@ssw0rd',
        # 'remember_me': 'true'
    })

    # 新添加评论请求
    res_data_a1 = post('/comment/add', {'content': 'aaa1'}, headers=NEW_HEADERS)
    assert res_data['code'] == const.SYS_SUCCESS.code
    assert len(res_data['data']) == 1


    res_data_b1 = post('/comment/add', {
        'content': 'bbb1',
        'parent_id': res_data_a1['data']['comment_id']
    }, headers=NEW_HEADERS)

    res_data_b2 = post('/comment/add', {
        'content': 'bbb2',
        'parent_id': res_data_a1['data']['comment_id']
    }, headers=NEW_HEADERS)

    res_data_c1 = post('/comment/add', {
        'content': 'ccc1',
        'parent_id': res_data_b1['data']['comment_id']
    }, headers=NEW_HEADERS)

    res_data_c2 = post('/comment/add', {
        'content': 'ccc2',
        'parent_id': res_data_b1['data']['comment_id']
    }, headers=NEW_HEADERS)

    res_data_c3 = post('/comment/add', {
        'content': 'ccc3',
        'parent_id': res_data_b2['data']['comment_id']
    }, headers=NEW_HEADERS)

    # 获取评论树
    res_data = get('/comment/tree', {'comment_id': res_data_a1['data']['comment_id']}, headers=HEADERS)
    assert res_data['code'] == const.SYS_SUCCESS.code
    assert len(res_data['data']) == 1
    assert len(res_data['data'][0]['children']) == 2
    assert len(res_data['data'][0]['children'][0]['children']) == 1
    assert len(res_data['data'][0]['children'][1]['children']) == 2
    #    1
    #    /\
    #   2  5
    #  /\   \
    # 3  4   6