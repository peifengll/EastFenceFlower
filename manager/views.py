import json

from django.shortcuts import render

# Create your views here.
from datetime import datetime

from django.db.models import Q
from django.utils import timezone

from rest_framework.views import APIView
from django.db import connection
import models.models
from libs.utils.base_response import BaseResponse
from manager import serializer


# 分页了
class ShowManagersInfo(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        pagetotal = 6
        pagenum = int(request.GET.get("page", 1))
        offset = (pagenum - 1) * pagetotal
        print("page:", pagenum)
        with connection.cursor() as cursor:
            sql = "select * from manager limit %s offset %s"
            cursor.execute(sql, [pagetotal, offset])
            raw_data = cursor.fetchall()
            # 将元组列表转换为字典列表
            data_dict_list = [dict(zip([col[0] for col in cursor.description], row)) for row in raw_data]
        ser = serializer.ManagerShowSerializer(data_dict_list, many=True)
        return BaseResponse(data=ser.data, status=200, )


class ShowAllManagersInfo(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        with connection.cursor() as cursor:
            sql = "select * from manager "
            cursor.execute(sql)
            raw_data = cursor.fetchall()
            # 将元组列表转换为字典列表
            data_dict_list = [dict(zip([col[0] for col in cursor.description], row)) for row in raw_data]
        ser = serializer.ManagerShowSerializer(data_dict_list, many=True)
        return BaseResponse(data=ser.data, status=200, )


class ManagerDelView(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def delete(self, request, *args, **kwargs):
        mids = request.GET.get("manager_ids")
        # print("122222222222222222")
        mids = json.loads(mids)
        # print(mids[0])
        # print(mids[0])
        # print(mids[1])
        # print(mids[2])

        # print("122222222222222222")
        if not mids:
            return BaseResponse(data="", status=400, msg="manager_ids 不能为空")
        try:
            models.models.Manager.objects.filter(manager_id__in=mids).delete()
        except models.models.User.DoesNotExist:
            return BaseResponse(status=322, msg="店员账户不存在")
        except Exception as e:
            print(e.__str__())
            return BaseResponse(data="", status=500, msg="删除失败")
        return BaseResponse(status=200, msg="删除成功")


class ManagerAddView(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def post(self, request, *args, **kwargs):
        mname = request.data.get("mname")
        phone = request.data.get("phone")
        password = request.data.get("password")
        photo = request.data.get("photo")
        days = request.data.get("days")
        address = request.data.get("address")
        restrict = request.data.get("restrict")
        sex = request.data.get("sex")
        age = request.data.get("age")
        stage = request.data.get("stage")
        try:
            models.models.Manager.objects.create(
                mname=mname,
                phone=phone,
                password=password,
                photo=photo,
                days=days,
                address=address,
                restrict=restrict,
                sex=sex,
                age=age,
                stage=stage,
                date=datetime.now(),
            )
        except Exception as e:
            return BaseResponse(status=500, msg="服务器内部错误" + e.__str__())
        return BaseResponse(status=200, msg="添加成功")


class ManagerUpdateView(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def put(self, request, *args, **kwargs):
        manager_id = request.data.get("manager_id")
        if not manager_id:
            return BaseResponse(data="", status=400, msg="manager_id 不能为空")
        mname = request.data.get("mname")
        phone = request.data.get("phone")
        password = request.data.get("password")
        photo = request.data.get("photo")
        days = request.data.get("days")
        address = request.data.get("address")
        restrict = request.data.get("restrict")
        sex = request.data.get("sex")
        age = request.data.get("age")
        stage = request.data.get("stage")
        try:
            obj = models.models.Manager.objects.get(manager_id=manager_id)
            if mname:
                obj.mname = mname
            if phone:
                obj.phone = phone
            if password:
                obj.password = password
            if photo:
                obj.photo = photo
            if days:
                obj.days = days
            if address:
                obj.address = address
            if restrict:
                obj.restrict = restrict
            if sex:
                obj.sex = sex
            if age:
                obj.age = age
            if stage:
                obj.stage = stage
            obj.save()
        except Exception as e:
            return BaseResponse(status=500, msg="服务器内部错误" + e.__str__())
        return BaseResponse(status=200, msg="修改成功")
