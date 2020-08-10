from rest_framework import serializers
from .models import StudyMember


class StudyMemberSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='user.user_id')
    name = serializers.ReadOnlyField(source='user.name')
    email = serializers.ReadOnlyField(source='user.email')
    birthday = serializers.ReadOnlyField(source='user.birthday')
    cellphone = serializers.ReadOnlyField(source='user.cellphone')
    gender = serializers.ReadOnlyField(source='user.gender')

    class Meta:
        model = StudyMember
        fields = ['is_manager', 'id', 'name', 'email', 'birthday', 'cellphone', 'gender', ]


class UserStudySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='study.study_id')
    title = serializers.ReadOnlyField(source='study.title')

    class Meta:
        model = StudyMember
        fields = ['id', 'title']
