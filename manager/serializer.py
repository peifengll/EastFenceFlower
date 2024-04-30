from rest_framework import serializers

from models.models import Manager


class ManagerShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        exclude = ['password']
        # fields = '__all__'
