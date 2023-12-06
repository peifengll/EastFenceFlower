#!/user/bin/env python3
# -*- coding: utf-8 -*-
from rest_framework import exceptions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from login.models import Manager

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import exceptions

from django.utils.translation import gettext_lazy as _


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super(MyTokenObtainPairSerializer, cls).get_token(user)
#
#         # Add custom claims
#         token['username'] = user.username
#         return token
#

class LoginSerializer(TokenObtainPairSerializer):
    class Meta:
        model = Manager
        fields = "__all__"
        read_only_fields = ["id"]

    default_error_messages = {
        'no_active_account': '该账号已被禁用,请与管理员联系!'
    }

    def validate(self, attrs):
        phone = attrs['phone']
        password = attrs['password']
        user = Manager.objects.filter(phone=phone).first()
        if not user:
            result = {
                "code": 400,
                "msg": "账号或密码不正确！",
                "data": None
            }
            return result

        if user and not user.is_staff:  # 判断是否允许登录后台
            result = {
                "code": 400,
                "msg": "您没有权限登录后台！",
                "data": None
            }
            return result

        if user and not user.is_active:
            result = {
                "code": 400,
                "msg": "该账号已被禁用,请与管理员联系！",
                "data": None
            }
            return result

        if user and user.check_password(password):  # check_password() 对明文进行加密,并验证
            # data = super().validate(attrs)
            refresh = self.get_token(self.user)
            data = {}
            # data['username'] = self.user.username
            data['userId'] = self.user.id
            data['refresh'] = str(refresh)  # refresh_token
            data['access'] = str(refresh.access_token)  # access_token
            request = self.context.get('request')
            request.user = self.user
            result = {
                "code": 200,
                "msg": "登录成功！",
                "data": data
            }
        else:
            result = {
                "code": 400,
                "msg": "账号或密码不正确！",
                "data": None
            }
        return result


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    自定义登录认证，使用自有用户表
    """
    phone_field = 'phone'

    def validate(self, attrs):
        authenticate_kwargs = {self.phone_field: attrs[self.username_field], 'password': attrs['password']}
        print(authenticate_kwargs)
        try:
            user = Manager.objects.get(**authenticate_kwargs)
        except Exception as e:
            raise exceptions.NotFound(e.args[0])

        refresh = self.get_token(user)

        data = {"userId": user.id, "token": str(refresh.access_token), "refresh": str(refresh)}
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class MyJWTAuthentication(JWTAuthentication):
    '''
    修改JWT认证类，返回自定义User表对象
    '''

    def get_user(self, validated_token):
        try:
            user_id = validated_token['user_id']
        except KeyError:
            raise InvalidToken(_('Token contained no recognizable user identification'))

        try:
            user = Manager.objects.get(**{'id': user_id})
        except Manager.DoesNotExist:
            raise AuthenticationFailed(_('User not found'), code='user_not_found')

        return user
