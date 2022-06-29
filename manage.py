# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""
#from flask_script import Manager
from flask_migrate import Migrate

from flask_app import app, db
from util.file import package_import


#
package_import('model')

# 让python支持命令行工作
# manager = Manager(app)

# 使用migrate绑定app和db
migrate = Migrate(app, db)



# if __name__ == '__main__':
#     app.run()
    # manager.run()
