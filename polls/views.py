from django.shortcuts import render
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.


def create(self, validated_data):
    # 获取登录用户user
    user = validated_data['user']
    # 设置最新登录时间
    user.last_login = timezone.now()
    user.save()

    refresh = RefreshToken.for_user(user)
    # 给user对象增加属性，保存jwt token的数据
    user.refresh = str(refresh)
    user.token = str(refresh.access_token)

    return user
