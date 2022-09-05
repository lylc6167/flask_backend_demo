import multiprocessing
import os

bind = '0.0.0.0:8080'

# 进程数
# workers = multiprocessing.cpu_count() * 2 + 1
workers = multiprocessing.cpu_count()

# 每个进程的线程数
threads = 4
# 工作模式
worker_class = 'gevent'
# 每个进程的最大链接数（并发量）
worker_connection = 1000
# 进程pid文件
pidfile = '/var/run/gunicorn.pid'
# 日志路径(容器内的绝对路径)
accesslog = '/log/gunicorn_access.log'
errorlog = '/log/gunicorn_error.log'
# 日志级别
capture_output = True
# 代码变更是否自动重启
reload = True