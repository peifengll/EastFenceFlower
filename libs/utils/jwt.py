#!/user/bin/env python3
# -*- coding: utf-8 -*-

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from django.utils.translation import gettext_lazy as _
from login.models import Manager


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
            user.password = ''
        except Manager.DoesNotExist:
            raise AuthenticationFailed(_('User not found'), code='user_not_found')
        return user
