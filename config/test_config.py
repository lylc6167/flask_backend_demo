# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""

# jwt配置
jwt_cnf = {
    "key_len": 8,
    "token_key": "tk_"
}

# redis有效时间配置
ex_time = {
    'captcha_ex': 2 * 60,
    'session_ex': 30 * 30,
    'token_ex': 30 * 24 * 60 * 60
}

db_config = {
    "url": "postgresql+psycopg2://comment6167:Tree2022@localhost/comment_db",
    # "pool_size": 1,
    # "max_overflow": 10,
    # "pool_recycle": 2 * 60 * 60
}

