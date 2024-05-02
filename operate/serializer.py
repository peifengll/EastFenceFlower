from rest_framework import serializers

from models import models


class OperateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Operate
        fields = '__all__'
