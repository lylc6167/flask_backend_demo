# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""


web = {
    "url_pre": "",
    "api_version": ["v1"],
    "ip": "0.0.0.0",
    "port": 8080,

}

# jwt配置
jwt_conf = {
    "key_len": 8,
    "token_key": "tk_hakunamatata"
}

# redis有效时间配置
ex_time = {
    'captcha_ex': 2 * 60,
    'session_ex': 30 * 30,
    'token_short_ex': 24 * 60 * 60,
    'token_long_ex': 30 * 24 * 60 * 60
}

# 主数据库config
db_config = {
    "url": "postgresql+psycopg2://comment6167:Tree2022@localhost/comment_db",
    # "pool_size": 1,
    # "max_overflow": 10,
    # "pool_recycle": 2 * 60 * 60
}

