# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""
import json
# import simplejson as json

from flask import current_app

from const import Code


def build_ret(code: Code, total=0, data: list = None):
    """
    生成请求响应json
    :param code: type(dict) 信息
    :param total: type(int) 数据总数(用于分页)
    :param data: type(list) 数据
    :return: format of json is:
    {
        "data": []
        "total": 0,
        "msg": "",
        "code": 0
    }
    """
    if data is None:
        data = []
    dic = {
        "data": data,
        "total": total,
        "msg": code.msg,
        "code": code.code
    }
    # 处理data里的None 转换为空字符串
    tran_none_data(data)
    return current_app.response_class(
        (json.dumps(dic, ensure_ascii=False)),
        mimetype=current_app.config['JSONIFY_MIMETYPE']
    )


def build_ret_one(code: Code, data: dict = None, sec_msg: str = None):
    """
    生成请求响应json
    :param code: 错误类
    :param data: 数据
    :return: format of json is:
    {
        "data": {}
        "msg": "",
        "code": 0
    }
    """
    if data is None:
        data = {}
    msg = "%s%s" % (code.msg, sec_msg) if sec_msg else code.msg
    dic = {
        "data": data,
        "msg": msg,
        "code": code.code
    }
    # 处理data里的None 转换为空字符串
    tran_none_data(data)
    return current_app.response_class(
        (json.dumps(dic, ensure_ascii=False)),
        mimetype=current_app.config['JSONIFY_MIMETYPE']
    )


def tran_none_data(dic_json):
    """
    原来的data中可能存在json格式数据，所以在转换为json格式数据后再转回dict做空元素处理
    :param dic_json:
    :return:
    """
    if isinstance(dic_json, dict):
        for key in dic_json:
            fill_data(dic_json, key)
    elif isinstance(dic_json, list):
        for data in dic_json:
            for key in data:
                fill_data(data, key)


def fill_data(dic_json: dict, key):
    if isinstance(dic_json[key], list):
        for li in dic_json[key]:
            tran_none_data(li)
    elif dic_json[key] is None or dic_json[key] == 'None':
        dic_json[key] = ""


def get_g():
    g_proxy = object()
    try:
        from flask import g
        g_proxy = g
        g_proxy.info = True
    except Exception as e:
        pass
    finally:
        return g_proxy


def tran_bool(data):
    if data.lower() == str(True).lower():
        return True
    elif data.lower() == str(False).lower():
        return False
    return None
