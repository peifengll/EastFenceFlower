from django.shortcuts import render

# Create your views here.

from django.db import connection
from django.db.models import Q
from django.shortcuts import render
from rest_framework.views import APIView

import models.models
from libs.utils.base_response import BaseResponse


class OperateUpdateView(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def put(self, request, *args, **kwargs):
        op_id = request.data.get("op_id")
        op_name = request.data.get("op_name")
        gname = request.data.get("gname")
        goods_id = request.data.get("goods_id")
        size = request.data.get("size")
        op_time = request.data.get("op_time")
        op_num = request.data.get("op_num")
        op_person = request.data.get("op_person")
        op_person_id = request.data.get("op_person_id")
        op_otherS = request.data.get("op_otherS")
        try:
            ovj = models.models.Operate.objects.get(op_id=op_id)
            if op_name:
                ovj.op_name = op_name
            if gname:
                ovj.gname = gname
            if goods_id:
                ovj.goods_id = goods_id
            if size:
                ovj.size = size
            if op_time:
                ovj.op_time = op_time
            if op_num:
                ovj.op_num = op_num
            if op_person:
                ovj.op_person = op_person
            if op_person_id:
                ovj.op_person_id = op_person_id
            if op_otherS:
                ovj.op_otherS = op_otherS
            ovj.save()
        except Exception as e:
            print(e.__str__())
            return BaseResponse(status=500, msg="服务器内部错误" + e.__str__())
        return BaseResponse(status=200, msg="修改成功")


class OperateAddView(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def post(self, request, *args, **kwargs):
        op_name = request.data.get("op_name")
        gname = request.data.get("gname")
        goods_id = request.data.get("goods_id")
        size = request.data.get("size")
        op_time = request.data.get("op_time")
        op_num = request.data.get("op_num")
        op_person = request.data.get("op_person")
        op_person_id = request.data.get("op_person_id")
        op_other = request.data.get("op_other")
        try:
            models.models.Operate.objects.create(
                op_name=op_name,
                gname=gname,
                goods_id=goods_id,
                size=size,
                op_time=op_time,
                op_num=op_num,
                op_person=op_person,
                op_person_id=op_person_id,
                op_other=op_other,
            )
        except Exception as e:
            print(e.__str__())
            return BaseResponse(status=500, msg="服务器内部错误" + e.__str__())
        return BaseResponse(status=200, msg="操作成功")
