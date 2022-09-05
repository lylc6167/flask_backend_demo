# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""
import os


prj_env = os.environ.get('PRJ_ENV')
if prj_env == 'prod':
    from config.prod_config import *
elif prj_env == 'test':
    from config.test_config import *
else:
    from config.local_config import *
