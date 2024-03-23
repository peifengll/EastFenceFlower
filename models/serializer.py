#!/user/bin/env python3
# -*- coding: utf-8 -*-
from rest_framework import serializers

import models.models


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.models.Order
        fields = '__all__'


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.models.Goods
        fields = '__all__'


class GoodSerializerFirstThree(serializers.ModelSerializer):
    class Meta:
        model = models.models.Goods
        fields = ('gname', 'salenum', 'image', 'ename', 'goods_id')


class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.models.Flower
        fields = '__all__'
