# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""
from datetime import datetime, timedelta, date


def datetime_format(dt: datetime = None, fmt="%Y-%m-%d %H:%M:%S"):
    """
    时间格式化
    :param dt:
    :param fmt:
    :return:
    """
    if dt is None:
        # dt = datetime.now()
        return ''
    return dt.strftime(fmt)


def date_format(dt: datetime=None, fmt='%Y-%m-%d'):
    if dt is None:
        return ''
    return dt.strftime(fmt)

def str_to_date(dt_str: str):
    dt_list = [int(i) for i in dt_str.split('/')]
    return date(dt_list[0], dt_list[1], dt_list[2])
