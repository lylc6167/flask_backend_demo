# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""


from enum import IntEnum


class SpecialRuleEnum(IntEnum):
    # 特殊规则码

    NO_LIMIT = 0  # 无限制
    DELIVERY = 1  # 仅配送
    SALE = 2  # 仅外销



