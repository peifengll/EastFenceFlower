#!/user/bin/env python3
# -*- coding: utf-8 -*-
from rest_framework import serializers

import models.models


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.models.Order
        fields = '__all__'
