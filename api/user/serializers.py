from rest_framework import serializers
from .models import User
from ..study.serializers import StudySerializer
from ..study_member.models import StudyMember


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'email', 'name', 'age', 'cellphone', 'gender', 'description', 'categories',
                  'kakao_profile_img','s3_profile_img','img_flag',]


class UserStudySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='study.study_id')
    title = serializers.ReadOnlyField(source='study.title')

    class Meta:
        model = StudyMember
        fields = ['id', 'title']


class UserDetailSerializer(serializers.ModelSerializer):
    study_list = UserStudySerializer(source='studymember_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'email', 'name', 'age', 'cellphone', 'gender', 'description', 'categories', 'study_list',
                  'kakao_profile_img','s3_profile_img','img_flag',]
