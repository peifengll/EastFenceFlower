#!/user/bin/env python3
# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Manager


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = (
            'manager_id',
            'mname',
            'phone',
            'password',
            'photo',
            'days',
            'address',
            'restrict',
            'sex',
            'age',
            'stage',
            'date',
        )

