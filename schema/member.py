# encoding: utf-8
"""
@version: 1.0
@author: 6167
@contact: 6167.good@gmail.com
@time: 2022-05-19 15:00
"""
import re

from marshmallow import Schema, fields, post_load, ValidationError, validates
from model.member import Member

class MemberSingupSchema(Schema):
    """
    username需要检查：不可为空，只能使用字母和数字，长度在5~20之间，不能与已有用户名重复(后端)
    password需要检查：不可为空，长度在8~20之间，至少包含一个大写、一个小写、一个数字、一个特殊符号(前端)
    email需要检查：不可为空，格式要正确，不能与已有email重复。为简单起见，不需要发送邮件确认(后端)
    """
    # 用户名
    username = fields.Str(required=True)
    # 密码
    password = fields.Str(required=True)
    # 邮箱
    email = fields.Email(required=True)

    @post_load
    def make_attr_name(self, data, **kwargs):  # marshmellow 3.0版本之后新增参数
        return Member(**data)

    @validates("username")
    def validate_name(self, value):
        if not re.match('^[0-9a-zA-Z]{5,20}$', value):
            raise ValidationError("username只能包含字母和数字，长度在5~20之间")

    # @validates("password")
    # def validate_password(self, value):
    #     if not re.match('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,20}$', value):
    #         raise ValidationError("password必须包含大、小写、数字、特殊符号,长度在8~20之间")



class MemberLoginSchema(Schema):
    # 用户名
    username = fields.Str(required=True)
    # 密码
    password = fields.Str(required=True)
    # 是否记住
    remember_me = fields.Boolean(required=False)
