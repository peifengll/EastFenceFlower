#!/user/bin/env python3
# -*- coding: utf-8 -*-
from rest_framework import serializers

from models.models import User

'''
编号，姓名，性别，年龄，等级，电话，地址
'''


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['user_id', 'uname', 'sex', 'age', 'stage', 'phone', 'address']


class UserNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'photo', 'uname', 'sex', 'age', 'stage', 'phone', 'address']
