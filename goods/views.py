from django.shortcuts import render
from rest_framework.views import APIView

from libs.utils.base_response import BaseResponse
from models import models
from models.serializer import GoodSerializer, GoodSerializerFirstThree


# Create your views here.

# 查询全部商品
class GoodsAllInfo(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        info = models.Goods.objects.all()
        print(info)
        ser = GoodSerializer(info, many=True)
        return BaseResponse(data=ser.data, status=200, )


class GoodsOneInfoById(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        id = request.GET.get('goodsid')
        if id is None:
            return BaseResponse(status=400, msg="参数错误")
        info = models.Goods.objects.get(goods_id=id)
        print(info)
        ser = GoodSerializer(info)
        return BaseResponse(data=ser.data, status=200, msg="操作成功")


#  按照id  名字 分类进行查询
class GoodsInfoSearch(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        id = request.GET.get('goodsid')
        name = request.GET.get('goodsname')
        category = request.GET.get('goodsort')
        if id is None:
            return BaseResponse(status=400, msg="参数错误")
        info = models.Goods.objects.filter(goods_id=id)
        print(info)
        ser = GoodSerializer(info)
        return BaseResponse(data=ser.data, status=200, msg="操作成功")


class GoodsAdd(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def post(self, request, *args, **kwargs):
        goodsort = request.data.get("good_sort")
        gname = request.data.get("gname")
        flowerid = request.data.get("flower_id")
        image = request.data.get("image")
        ename = request.data.get("ename")
        size = request.data.get("size")
        charge = request.data.get("charge")
        tonum = request.data.get("total_num")
        stage = request.data.get("stage")
        salenum = "0"
        try:
            info = models.Goods.objects.create(
                good_sort=goodsort,
                gname=gname,
                flower_id=flowerid,
                image=image,
                ename=ename,
                size=size,
                charge=charge,
                total_num=tonum,
                stage=stage,
                salenum=salenum,
            )
            print("into" * 5)
            print(info)
            print("into" * 5)

        except Exception as e:
            print(e)
            return BaseResponse(status=500, msg=e.__str__())
        return BaseResponse(status=200, msg="操作成功")


class GoodsUpdate(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def put(self, request, *args, **kwargs):
        good_id = request.data.get("good_id")
        if not good_id:
            return BaseResponse(status=500, msg="缺少必要参数")
        goodsort = request.data.get("good_sort")
        gname = request.data.get("gname")
        flowerid = request.data.get("flower_id")
        image = request.data.get("image")
        ename = request.data.get("ename")
        size = request.data.get("size")
        charge = request.data.get("charge")
        tonum = request.data.get("total_num")
        stage = request.data.get("stage")
        salenum = request.data.get("salenum")
        try:
            obj = models.Goods.objects.get(goods_id=good_id)
            if goodsort is not None and goodsort != "":
                obj.good_sort = goodsort
            if gname is not None and gname != "":
                obj.gname = gname
            if flowerid is not None and flowerid != "":
                obj.flower_id = flowerid
            if image is not None and image != "":
                obj.image = image
            if ename is not None and ename != "":
                obj.ename = ename
            if size is not None and size != "":
                obj.size = size
            if charge is not None and charge != "":
                obj.charge = charge
            if tonum is not None and tonum != "":
                obj.total_num = tonum
            if stage is not None and stage != "":
                obj.stage = stage
            if salenum is not None and salenum != "":
                obj.sale_num = salenum
            obj.save()

        except Exception as e:
            print(e)
            return BaseResponse(status=500, msg=e.__str__())
        return BaseResponse(status=200, msg="操作成功")


class GoodsDeleteById(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def delete(self, request, *args, **kwargs):
        id = request.GET.get('goodsid')
        if id is None:
            return BaseResponse(status=400, msg="参数错误")
        try:
            info = models.Goods.objects.filter(goods_id=id).delete()
            print(info)
        except  Exception as e:
            print(e.__str__())
            return BaseResponse(status=500, msg=e.__str__())
        return BaseResponse(status=200, msg="操作成功")



#  销量前三名
class GoodsFirstThree(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        info = models.Goods.objects.order_by('-salenum')[:3]
        print(info)
        ser = GoodSerializerFirstThree(info, many=True)
        return BaseResponse(data=ser.data, status=200, msg="操作成功")
