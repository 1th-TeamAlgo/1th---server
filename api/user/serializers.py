from rest_framework import serializers
from .models import User
from ..study_member.serializers import UserStudySerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'email', 'name', 'age', 'cellphone', 'gender', 'categories']


class UserDetailSerializer(serializers.ModelSerializer):
    study_list = UserStudySerializer(source='studymember_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'email', 'name', 'age', 'cellphone', 'gender', 'categories', 'study_list']
