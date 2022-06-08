# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""
# from flask import Blueprint

from flask_app.app import db, app
# from flask_app.error_handle import *
from util.file import package_import

# order_bp = Blueprint('order', __name__, url_prefix='/order')

package_import("route")
package_import("intercept")
# # 读取数据库需要
# package_import("model")

# app.register_blueprint(order_bp)

