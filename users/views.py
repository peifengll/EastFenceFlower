from django.db.models import Q
from django.utils import timezone

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connection

import models.models
import users.serializer
from libs.utils.base_response import BaseResponse
from users import serializer


# Create your views here.


class ShowUsersInfo(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        pagetotal = 6
        pagenum = int(request.GET.get("page", 1))
        offset = (pagenum - 1) * pagetotal
        print("page:", pagenum)
        with connection.cursor() as cursor:
            sql = "select * from user limit %s offset %s"
            cursor.execute(sql, [pagetotal, offset])
            raw_data = cursor.fetchall()
            # 将元组列表转换为字典列表
            data_dict_list = [dict(zip([col[0] for col in cursor.description], row)) for row in raw_data]
        ser = users.serializer.UserSerializer(data_dict_list, many=True)
        return BaseResponse(data=ser.data, status=200, )


class ShowNewUsersToday(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        today = timezone.now().date()
        print("today:", today)
        pagetotal = 6
        pagenum = int(request.GET.get("page", 1))
        offset = (pagenum - 1) * pagetotal
        print("page:", pagenum)
        with connection.cursor() as cursor:
            sql = "select * from user where time=%s limit %s offset %s"
            cursor.execute(sql, [today, pagetotal, offset])
            raw_data = cursor.fetchall()
            # 将元组列表转换为字典列表
            data_dict_list = [dict(zip([col[0] for col in cursor.description], row)) for row in raw_data]
        ser = users.serializer.UserNewSerializer(data_dict_list, many=True)
        return BaseResponse(data=ser.data, status=200, )

        # userList = models.models.User.objects.filter(time=today)
        # ser = users.serializer.UserNewSerializer(userList, many=True)
        #
        # return BaseResponse(data=ser.data, status=200, )


class ShowNewUsersTodayNum(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        today = timezone.now().date()
        print("today:", today)
        num = models.models.User.objects.filter(time=today).count()
        return BaseResponse(data=num, status=200, )

        # userList = models.models.User.objects.filter(time=today)
        # ser = users.serializer.UserNewSerializer(userList, many=True)
        #
        # return BaseResponse(data=ser.data, status=200, )


class UserSearch(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        #  返回stage为0022的订单，也就是待备货
        # print("*" * 5)
        user_id = request.GET.get("user_id")
        uname = request.GET.get("uname")
        userAge = request.GET.get("userAge")
        userPhone = request.GET.get("userPhone")
        # print(user_id, userAge, userPhone, uname)
        # print("*" * 5)
        # 初始化查询条件
        # 初始化查询条件
        query_params = Q()

        # 如果某一项不为空，就添加该条件到查询中
        if user_id:
            query_params &= Q(user_id=user_id)
        if uname:
            query_params &= Q(uname=uname)
        if userAge:
            query_params &= Q(age=userAge)
        if userPhone:
            query_params &= Q(phone=userPhone)
        userList = models.models.User.objects.filter(query_params)

        # print("userlist", userList)
        ser = serializer.UserSerializer(userList,many=True)
        return BaseResponse(data=ser.data, status=200, )
