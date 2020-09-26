from rest_framework import serializers
from ..models import User


class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', ]
