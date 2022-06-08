#数据库指令：
######测试数据库版本 psql10.3
````cmd
# 进入数据库cmd
psql -U postgres -h localhost
# 创建用户
create user comment6167 with password 'Tree2022';
# 创建数据库
create database comment_db owner comment6167;
# 赋权
grant all privileges on database comment_db to comment6167;

````

# 安装依赖包
```cmd
# 进入后端项目路径
cd .../../backend
# pip安装
pip install -r requirements.txt
```

#数据库 初始化建表
````cmd
# 设置flask_app环境变量
set FLASK_APP=manage.py
# 进入shell命令行
>>flask shell
# 首次创建主数据库
>>>from manage import db
>>>db.create_all(bind=None)
````

# 数据库后续migrate
######新版本flask-migrate不支持flask-script（4年没更新）
````cmd
# 设置flask_app环境变量
set FLASK_APP=manage.py
# 初始化migration文件夹，和数据库迁移脚本
flask db init
# 创建迁移脚本
flask db migrate -m "message"
# 更新数据库
flask db upgrade
# 之后操作重复migrate&upgrade


````

# 开发模式启动服务
````cmd
# 设置flask_app环境变量
set FLASK_APP=manage.py
# 启动服务
flask run


````

#ngnix部署
````cmd
# 解压缩ngnix文件夹到D://，命令行进入 cd
# 编辑conf/ngnix.conf文件下的http节点，修改server/listen为8080端口号
# cmd在ngnix目录下，启动指令:start nginx
# 检查是否成功：nginx -t -c /nginx/conf/nginx.conf
# 成功后再启动：nginx -s reload

````


#注册ngnix和flask应用程序到服务中


#使用winsw注册服务到系统中
````cmd
# 查看当前系统的.netframework版本，本机为4.0
# 
````

