from rest_framework import serializers
from .models import StudyMember


class StudyMemberSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.user_id')
    email = serializers.ReadOnlyField(source='user.email')
    name = serializers.ReadOnlyField(source='user.name')
    age = serializers.ReadOnlyField(source='user.age')
    cellphone = serializers.ReadOnlyField(source='user.cellphone')
    gender = serializers.ReadOnlyField(source='user.gender')
    description = serializers.ReadOnlyField(source='user.description')
    categories = serializers.ReadOnlyField(source='user.categories')
    kakao_profile_img = serializers.ReadOnlyField(source='user.kakao_profile_img')
    s3_profile_img = serializers.FileField(source='user.s3_profile_img')
    img_flag = serializers.ReadOnlyField(source='user.img_flag')

    class Meta:
        model = StudyMember
        fields = ['study_member_id', 'study', 'is_manager', 'user_id', 'name', 'email', 'age', 'cellphone', 'gender',
                  'description','categories','kakao_profile_img', 's3_profile_img', 'img_flag', ]


class StudyMemberDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMember
        fields = ['study', 'user', ]


class StudyAddStudyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMember
        fields = ['study', 'user', 'is_manager' ]


