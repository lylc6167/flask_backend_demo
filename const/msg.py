# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""


class Code(Exception):
    def __init__(self, code: int, msg: str):
        self.code = code
        self.msg = msg


# common
SYS_SUCCESS = Code(code=0, msg=u"操作成功")
SYS_FAIL = Code(code=1, msg=u"操作失败")

# common error
SYS_RECORD_NOT_FOUND = Code(code=9991, msg=u"记录不存在")
SYS_NAME_REPEATED_ERROR = Code(code=9992, msg=u"名称重复")
SYS_INVALID_REQUEST = Code(code=9993, msg=u"错误的请求")
SYS_NOT_FOUND = Code(code=9994, msg=u"页面不存在")
CODE_SYS_ERROR = Code(9995, u"系统错误")
CODE_VALIDATE_ERROR = Code(9996, u"数据验证错误,请检查填写内容是否有误")
SYS_PARAMETER_ERROR = Code(code=9997, msg=u"参数错误")

# member error
MEMBER_ID_NOT_FOUND = Code(code=10001, msg=u"用户ID不存在")
MEMBER_USERNAME_NOT_FOUND = Code(code=10002, msg=u"登录用户名不存在")
MEMBER_OR_EMAIL_EXIST = Code(code=10003, msg=u"注册用户名或邮箱已存在")
MEMBER_LOGIN_PASSWORD_WRONG = Code(code=10004, msg=u"登录密码错误")
A_NO_AUTH = Code(code=10005, msg=u"权限不足")
A_TIMEOUT = Code(code=10006, msg=u"登录失效")
TOKEN_EXP_ERROR = Code(code=10007, msg=u"token过期失效")
TOKEN_DECODE_ERROR = Code(code=10008, msg=u"token认证失败")
TOKEN_INVALID_ERROR = Code(code=10009, msg=u"token非法")
NO_TOKEN_ERROR = Code(code=10010, msg=u"未携带token")

# comment error
COMMENT_PARENT_ID_NOT_FOUND = Code(code=11001, msg=u"评论的上级ID不存在")
COMMENT_ID_NOT_FOUND = Code(code=11002, msg=u"评论ID不存在")
