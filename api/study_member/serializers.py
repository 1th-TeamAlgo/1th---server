from rest_framework import serializers
from .models import StudyMember
from ..user.serializers import UserSerializer


class StudyMemberSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = StudyMember
        fields = ['study_member_id', 'study_id', 'user_id', 'is_manager', 'user_name']
