from rest_framework import serializers
from ...study_member.models import StudyMember


class UserStudySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='study.study_id')
    title = serializers.ReadOnlyField(source='study.title')

    class Meta:
        model = StudyMember
        fields = ['id', 'title']
