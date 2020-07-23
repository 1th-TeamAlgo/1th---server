from rest_framework import serializers
from .models import StudyMember

class StudyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMember
        fields = ['study_member_id', 'study_id', 'user_id','is_manager']


