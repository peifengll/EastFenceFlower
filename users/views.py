from datetime import datetime

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


class GetUsersPageTotal(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        pagetotal = 6
        num = models.models.User.objects.all().count()
        if num % pagetotal == 0:
            num = num // pagetotal
        else:
            num = num // pagetotal + 1
        return BaseResponse(data=num, status=200, )


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
        ser = serializer.UserSerializer(userList, many=True)
        return BaseResponse(data=ser.data, status=200, )


class UserAll(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        userList = models.models.User.objects.all()
        # print("userlist", userList)
        ser = serializer.UserSerializer(userList, many=True)
        return BaseResponse(data=ser.data, status=200, msg="查询成功")


class UserSearchView(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        name = request.GET.get("name")
        age = request.GET.get("age")
        user_id = request.GET.get("user_id")
        phone = request.GET.get("phone")
        # name = request.data.get("name")
        # age = request.data.get("age")
        # user_id = request.data.get("user_id")
        # phone = request.data.get("phone")

        try:
            query = Q()
            if name:
                query &= Q(uname__icontains=name)
            if age:
                query &= Q(age=age)
            if user_id:
                query &= Q(id=user_id)
            if phone:
                query &= Q(phone__icontains=phone)
            userList = models.models.User.objects.filter(query)
            print("sql: ")
            print(userList.query.__str__())
            ser = serializer.UserSerializer(userList, many=True)
        except Exception as e:
            return BaseResponse(data=None, status=500, msg="查询失败" + e.__str__())
        # print("userlist", userList)
        return BaseResponse(data=ser.data, status=200, msg="查询成功")


class UserDetail(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        userid = request.GET.get("userid")
        if not userid:
            return BaseResponse(data="", status=400, msg="userid 不能为空")
        try:
            userList = models.models.User.objects.get(user_id=userid)
        except Exception as e:
            return BaseResponse(data="", status=500, msg="查询失败")
        ser = serializer.UserNewSerializer(userList)
        return BaseResponse(data=ser.data, status=200, msg="查询成功")


class UserUpdate(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def put(self, request, *args, **kwargs):
        userid = request.data.get("user_id")
        if not userid:
            return BaseResponse(data="", status=400, msg="userid 不能为空")
        photo = request.data.get("photo")
        uname = request.data.get("uname")
        keyword = request.data.get("keyword")
        phone = request.data.get("phone")
        sex = request.data.get("sex")
        age = request.data.get("age")
        address = request.data.get("address")
        postnum = request.data.get("postnum")
        e_mail = request.data.get("e_mail")
        intor = request.data.get("intor")
        stage = request.data.get("stage")

        try:
            obj = models.models.User.objects.get(user_id=userid)
            if photo:
                obj.photo = photo
            if uname:
                obj.uname = uname
            if keyword:
                obj.keyword = keyword
            if phone:
                obj.phone = phone
            if sex:
                obj.sex = sex
            if age:
                obj.age = age
            if address:
                obj.address = address
            if postnum:
                obj.postnum = postnum
            if e_mail:
                obj.e_mail = e_mail
            if intor:
                obj.intor = intor
            if stage:
                obj.stage = stage
            obj.save()
        except Exception as e:
            return BaseResponse(data="", status=500, msg="修改失败" + e.__str__())
        return BaseResponse(status=200, msg="修改成功")


class UserDel(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def delete(self, request, *args, **kwargs):
        userid = request.GET.get("userid")
        if not userid:
            return BaseResponse(data="", status=400, msg="userid 不能为空")
        try:
            user = models.models.User.objects.get(user_id=userid)
            user.delete()
        except models.models.User.DoesNotExist:
            return BaseResponse(status=322, msg="用户不存在")
        except Exception as e:
            return BaseResponse(data="", status=500, msg="删除失败")
        return BaseResponse(status=200, msg="删除成功")


class UserFirstThree(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):

        try:
            user = models.models.User.objects.order_by("-cost")[:3]
        except Exception as e:
            return BaseResponse(data="", status=500, msg="查询失败")
        ser = serializer.UserNewSerializer(user, many=True)
        return BaseResponse(data=ser.data, status=200, msg="操作成功")


class UserAdd(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def post(self, request, *args, **kwargs):
        photo = request.data.get("photo")
        uname = request.data.get("uname")
        keyword = request.data.get("keyword")
        phone = request.data.get("phone")
        sex = request.data.get("sex")
        age = request.data.get("age")
        address = request.data.get("address")
        postnum = request.data.get("postnum")
        e_mail = request.data.get("e_mail")
        intor = request.data.get("intor")
        stage = request.data.get("stage")
        try:
            models.models.User.objects.create(
                photo=photo,
                uname=uname,
                keyword=keyword,
                phone=phone,
                sex=sex,
                age=age,
                address=address,
                time=datetime.now(),
                postnum=postnum,
                e_mail=e_mail,
                intor=intor,
                stage=stage,
                cost=0,
            )
        except Exception as e:
            return BaseResponse(status=500, msg="服务器内部错误" + e.__str__())
        return BaseResponse(status=200, msg="添加成功")
