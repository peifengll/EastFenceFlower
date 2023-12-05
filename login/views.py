import uuid

import redis
from django.shortcuts import render
from rest_framework.views import APIView

from login.models import Manager
from utils.base_response import BaseResponse
from rest_framework.response import Response

from utils.redis_pool import POOL


# Create your views here.


def login(request):
    request.session.clear()
    phone = request.GET.get('phone')
    password = request.GET.get('password')
    qsst = Manager.objects.filter(phone=phone, password=password)


class LoginView(APIView):
    def post(self, request):
        result = BaseResponse()
        phone = request.data.get('phone', '')
        password = request.data.get('password', '')
        user_obj = Manager.objects.filter(phone=phone, password=password)
        # 用户验证失败
        if not user_obj:
            result.code = 500
            result.error = "用户么或者密码错误"
            return Response(result.dict)
        # 用户验证成功，存入redis
        # 写入redis  token : user_id
        # conn = redis.Redis(connection_pool=POOL)

        try:
            token = uuid.uuid4()
            # conn.set(str(token), user_obj.id, ex=10)
            # conn.set(str(token), user_obj.id, ex=10)
            result.data = token
        except Exception as e:
            print(e)
            result.code = 501
            result.error = "创建令牌失败啦"
        return Response(result.dict)
