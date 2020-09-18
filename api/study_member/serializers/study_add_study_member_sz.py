from rest_framework import serializers
from ..models import StudyMember


class StudyAddStudyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMember
        fields = ['study', 'user', 'is_manager' ]


