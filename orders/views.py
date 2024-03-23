from django.db import connection
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
