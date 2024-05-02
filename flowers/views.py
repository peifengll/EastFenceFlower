import json

import numpy as np
from django.db.models import Q
from django.shortcuts import render
from rest_framework.views import APIView
import time as time_

from EastFenceFlower import settings
from libs.utils.base_response import BaseResponse
from models import models
from models.serializer import FlowerSerializer


# Create your views here.


class FlowerInfoSearch(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def get(self, request, *args, **kwargs):
        fid = request.GET.get('flowerid')
        name = request.GET.get('fname')
        sort = request.GET.get('sort')
        place = request.GET.get('place')
        season = request.GET.get('season')
        feed = request.GET.get('feed')
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
            if feed:
                query &= Q(feed=feed)
            if season:
                query &= Q(season=season)
            if place:
                query &= Q(brithplace__icontains=place)
            info = models.Flower.objects.filter(query)
            print(info.query.__str__())
        except Exception as e:
            print(e.__str__())
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
        fids = request.GET.get('flowerid')
        f_ids = json.loads(fids)
        print(f_ids)
        try:
            info = models.Flower.objects.filter(flower_id__in=f_ids)
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
            if buy:
                obj.buy = buy
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


class UploadImageView(APIView):
    authentication_classes = []  # 禁用所有认证类
    permission_classes = []  # 允许任何用户访问

    def post(self, request):
        print("request data ::", request.data)
        print('*' * 10)
        print("request file ::", request.FILES)

        # 获取一个文件管理器对象
        flowerid = request.data.get('flowerid')
        if flowerid is None or flowerid == "":
            return BaseResponse(msg="flowerid 不能为空未获取到", status=401)
        imagefile, image2file, image3file = None, None, None
        if 'image' in request.FILES:
            imagefile = request.FILES['image']
            print("image1 get")

        if 'image2' in request.FILES:
            image2file = request.FILES['image2']
            print("image2 get")

        if 'image3' in request.FILES:
            print("image3 get")
            image3file = request.FILES['image3']

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
        use = request.data.get("use")
        intor = request.data.get("intor")
        temp = request.data.get("temp")
        water = request.data.get("water")
        light = request.data.get("light")
        season = request.data.get("season")
        manure = request.data.get("manure")
        soil = request.data.get("soil")
        lop = request.data.get("lop")

        try:
            obj = models.Flower.objects.get(flower_id=flowerid)
            if fname:
                obj.fname = fname
            if enname:
                obj.enname = enname
            if buy:
                obj.buy = buy
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
            if imagefile is not None:
                file = imagefile
                new_name = getNewName('flower_img')  # 具体实现在自己写的uploads.py下
                # 将要保存的地址和文件名称
                where = '%s/flower/%s' % (settings.MEDIA_ROOT, new_name)
                # 分块保存image
                content = file.chunks()
                with open(where, 'wb') as f:
                    for i in content:
                        f.write(i)
                new_name = "/media/flower/" + new_name
                # 上传文件名称到数据库
                obj.image = new_name
                print(" image1 上传执行了吗： ", new_name)
            if image2file is not None:
                file = image2file
                new_name = getNewName('flower_img')  # 具体实现在自己写的uploads.py下
                # 将要保存的地址和文件名称
                where = '%s/flower/%s' % (settings.MEDIA_ROOT, new_name)
                # 分块保存image
                content = file.chunks()
                with open(where, 'wb') as f:
                    for i in content:
                        f.write(i)
                new_name = "/media/flower/" + new_name
                # 上传文件名称到数据库

                obj.image2 = new_name

                print("image2 上传执行了吗： ", new_name)
            if image3file is not None:
                file = image3file
                new_name = getNewName('flower_img')  # 具体实现在自己写的uploads.py下
                # 将要保存的地址和文件名称
                where = '%s/flower/%s' % (settings.MEDIA_ROOT, new_name)
                # 分块保存image
                content = file.chunks()
                with open(where, 'wb') as f:
                    for i in content:
                        f.write(i)
                new_name = "/media/flower/" + new_name
                # 上传文件名称到数据库

                obj.image3 = new_name
                print("image3 上传 执行了吗： ", new_name)

            obj.save()
            # 返回的httpresponse
        except Exception as e:
            print(e)
            return BaseResponse(msg="服务器内部错误", status=500)
        return BaseResponse(msg="返回成功", status=200, data={})


def getNewName(file_type):
    # 前面是file_type+年月日时分秒
    new_name = time_.strftime(file_type + '-%Y%m%d%H%M%S', time_.localtime())
    # 最后是5个随机数字
    # Python中的numpy库中的random.randint(a, b, n)表示随机生成n个大于等于a，小于b的整数
    ranlist = np.random.randint(0, 10, 5)
    for i in ranlist:
        new_name += str(i)
    # 加后缀名
    new_name += '.jpg'
    # 返回字符串
    return new_name
