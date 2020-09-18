from rest_framework import serializers
from ..models import StudyMember


class StudyMemberDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMember
        fields = ['study', 'user', ]
