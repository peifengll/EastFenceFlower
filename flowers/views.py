from django.db.models import Q
from django.shortcuts import render
from rest_framework.views import APIView

from libs.utils.base_response import BaseResponse
from models import models
from models.serializer import FlowerSerializer


# Create your views here.


class FlowerInfoSearch(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        fid = request.data.get('flowerid')
        name = request.data.get('fname')
        sort = request.data.get('sort')
        place = request.data.get('birthplace')
        info = None
        try:
            # 构建查询条件
            query = Q()
            if fid:
                query &= Q(flower_id=fid)
            if name:
                query &= Q(fname__icontains=name)
            if sort:
                query &= Q(sort=sort)
            if place:
                query &= Q(brithplace__icontains=place)
            info = models.Flower.objects.filter(query)
            print(info.query.__str__())
        except Exception as e:
            return BaseResponse(status=500, msg="服务器错误" + e.__str__())
        ser = FlowerSerializer(info, many=True)
        return BaseResponse(data=ser.data, status=200, msg="操作成功")


class FlowerAdd(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def post(self, request, *args, **kwargs):
        fname = request.data.get("fname")
        enname = request.data.get("enname")
        buy = request.data.get("buy")
        num = request.data.get("num")
        sort = request.data.get("sort")
        feed = request.data.get("feed")
        nickname = request.data.get("nickname")
        ldname = request.data.get("ldname")
        brithplace = request.data.get("brithplace")
        enplace = request.data.get("enplace")
        image = request.data.get("image")
        image2 = request.data.get("image2")
        image3 = request.data.get("image3")
        use = request.data.get("use")
        intor = request.data.get("intor")
        temp = request.data.get("temp")
        water = request.data.get("water")
        light = request.data.get("light")
        season = request.data.get("season")
        manure = request.data.get("manure")
        soil = request.data.get("soil")
        lop = request.data.get("lop")

        info = None
        try:
            models.Flower.objects.create(
                fname=fname,
                enname=enname,
                num=num,
                buy=buy,
                sort=sort,
                feed=feed,
                nickname=nickname,
                ldname=ldname,
                brithplace=brithplace,
                enplace=enplace,
                image=image,
                image2=image2,
                image3=image3,
                use=use,
                intor=intor,
                temp=temp,
                water=water,
                light=light,
                season=season,
                manure=manure,
                soil=soil,
                lop=lop,
            )
        except Exception as e:
            return BaseResponse(status=500, msg="服务器错误" + e.__str__())

        return BaseResponse(status=200, msg="操作成功")


class FlowerDel(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def delete(self, request, *args, **kwargs):
        fid = request.GET.get('flowerid')
        print(fid)
        try:
            info = models.Flower.objects.get(flower_id=fid)
            info.delete()
        except models.Flower.DoesNotExist:
            return BaseResponse(status=322, msg="要删除的对象不存在")
        except Exception as e:
            return BaseResponse(status=500, msg="服务器错误" + e.__str__())
        ser = FlowerSerializer(info, many=True)
        return BaseResponse(status=200, msg="操作成功")


class FlowerUpdate(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def put(self, request, *args, **kwargs):
        id = request.data.get("flowerid")
        if not id:
            return BaseResponse(status=317, msg="关键参数flowerid 缺失")
        fname = request.data.get("fname")
        enname = request.data.get("enname")
        buy = request.data.get("buy")
        num = request.data.get("num")
        sort = request.data.get("sort")
        feed = request.data.get("feed")
        nickname = request.data.get("nickname")
        ldname = request.data.get("ldname")
        brithplace = request.data.get("brithplace")
        enplace = request.data.get("enplace")
        image = request.data.get("image")
        image2 = request.data.get("image2")
        image3 = request.data.get("image3")
        use = request.data.get("use")
        intor = request.data.get("intor")
        temp = request.data.get("temp")
        water = request.data.get("water")
        light = request.data.get("light")
        season = request.data.get("season")
        manure = request.data.get("manure")
        soil = request.data.get("soil")
        lop = request.data.get("lop")

        info = None
        try:
            obj = models.Flower.objects.get(flower_id=id)
            if fname:
                obj.fname = fname
            if enname:
                obj.enname = enname
            if num:
                obj.num = num
            if sort:
                obj.sort = sort
            if feed:
                obj.feed = feed
            if nickname:
                obj.nickname = nickname
            if ldname:
                obj.ldname = ldname
            if brithplace:
                obj.brithplace = brithplace
            if enplace:
                obj.enplace = enplace
            if image:
                obj.image = image
            if image2:
                obj.image2 = image2
            if image3:
                obj.image3 = image3
            if use:
                obj.use = use
            if intor:
                obj.intor = intor
            if temp:
                obj.temp = temp
            if water:
                obj.water = water
            if light:
                obj.light = light
            if season:
                obj.season = season
            if manure:
                obj.manure = manure
            if soil:
                obj.soil = soil
            if lop:
                obj.lop = lop
            obj.save()
        except Exception as e:
            return BaseResponse(status=500, msg="服务器错误" + e.__str__())

        return BaseResponse(status=200, msg="操作成功")
