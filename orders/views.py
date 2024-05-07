import json

from django.db import connection
from django.db.models import Q
from django.shortcuts import render
from rest_framework.views import APIView

import models.models
from libs.utils.base_response import BaseResponse
from models import serializer
from models.serializer import OrderSerializer


# Create your views here.

#  需要做的订单
class OrdersToDo(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        #  返回stage为0022的订单，也就是待备货
        pagetotal = 6
        pagenum = int(request.GET.get("page", 1))
        offset = (pagenum - 1) * pagetotal
        print("page:", pagenum)
        with connection.cursor() as cursor:
            sql = "select * from order limit %s offset %s"  # todo order by 截止时间
            cursor.execute(sql, [pagetotal, offset])
            raw_data = cursor.fetchall()
            # 将元组列表转换为字典列表
            data_dict_list = [dict(zip([col[0] for col in cursor.description], row)) for row in raw_data]
        ser = serializer.OrderSerializer(data_dict_list, many=True)
        return BaseResponse(data=ser.data, status=200, )


#  需要做的订单的数量
class OrdersToDoNum(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        #  返回stage为0022的订单，也就是待备货
        a = models.models.Order.objects.filter(stage="0022").count()
        print(a)
        return BaseResponse(data=a, status=200, )


class OrdersToDeliverNum(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        #  返回stage为0022的订单，也就是待备货
        a = models.models.Order.objects.filter(stage="0023").count()
        print(a)
        return BaseResponse(data=a, status=200, )


class OrdersShowAll(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        #  返回stage为0022的订单，也就是待备货
        info = models.models.Order.objects.all()
        print(info)
        ser = OrderSerializer(info, many=True)
        return BaseResponse(data=ser.data, status=200, )


class OrdersOneById(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        id = request.GET.get("orderid")
        #  返回stage为0022的订单，也就是待备货
        info = models.models.Order.objects.get(order_id=id)
        print(info)
        ser = OrderSerializer(info)
        return BaseResponse(data=ser.data, status=200, )


class OrdersSearch(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        order_id = request.GET.get("order_id")
        stage = request.GET.get("stage")
        user_id = request.GET.get("user_id")
        phone = request.GET.get("phone")
        info = None
        try:
            query = Q()
            if order_id:
                query &= Q(order_id=order_id)
            if stage:
                query &= Q(stage=stage)
            if user_id:
                query &= Q(user_id=user_id)
            if phone:
                query &= Q(phone__icontains=phone)
            info = models.models.Order.objects.filter(query)
            # print("sss: ",info.query)
        except Exception as e:
            return BaseResponse(status=500, msg=e.__str__())
        ser = OrderSerializer(info, many=True)
        return BaseResponse(data=ser.data, status=200, )


# 修改 地址 状态
class OrdersUpdate(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def put(self, request, *args, **kwargs):
        order_id = request.data.get("order_id")
        if not order_id:
            return BaseResponse(status=400, msg="order_id不能为空")
        stage = request.data.get("stage")
        phone = request.data.get("phone")
        address = request.data.get("address")
        try:
            info = models.models.Order.objects.get(order_id=order_id)
            if stage:
                info.stage = stage
            if phone:
                info.phone = phone
            if address:
                info.address = address
            info.save()
            # print("sss: ",info.query)
        except Exception as e:
            return BaseResponse(status=500, msg=e.__str__())
        return BaseResponse(status=200, msg="修改成功")


class OrdersDel(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def delete(self, request, *args, **kwargs):
        order_ids = request.GET.get("order_id")
        oids = json.loads(order_ids)
        if not oids:
            return BaseResponse(status=400, msg="order_id不能为空")
        try:
            info = models.models.Order.objects.filter(order_id__in=oids)
            info.delete()
            # print("sss: ",info.query)
        except models.models.Order.DoesNotExist:
            return BaseResponse(status=322, msg="订单不存在")
        except Exception as e:
            return BaseResponse(status=500, msg=e.__str__())
        return BaseResponse(status=200, msg="删除成功")


# 利润
class OrderProfitView(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问
    def get(self, request, *args, **kwargs):
        a=Before7Days()
        print(a)
        return BaseResponse(status=200, msg="查询成功",data=a)


def Before7Days():
    sql = "SELECT DATE(time) as date, SUM(money) as total_money FROM `order` WHERE time >= DATE_SUB(CURDATE(), INTERVAL 7 DAY) GROUP BY DATE(time);"

    with connection.cursor() as cursor:
        cursor.execute(sql)
        raw_data = cursor.fetchall()
        # 将元组列表转换为字典列表
        data_dict_list = [dict(zip([col[0] for col in cursor.description], row)) for row in raw_data]
    return data_dict_list

def Before12Months():
    sql = "SELECT DATE(time) as date, SUM(money) as total_money FROM `order` WHERE time >= DATE_SUB(CURDATE(), INTERVAL 7 DAY) GROUP BY DATE(time);"

    with connection.cursor() as cursor:
        cursor.execute(sql)
        raw_data = cursor.fetchall()
        # 将元组列表转换为字典列表
        data_dict_list = [dict(zip([col[0] for col in cursor.description], row)) for row in raw_data]
    return data_dict_list

