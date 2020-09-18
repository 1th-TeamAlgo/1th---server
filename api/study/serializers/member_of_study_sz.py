from rest_framework import serializers
from ..models import Study
from ...study_member.serializers.study_member_sz import StudyMemberSerializer


class MemberOfStudySerializer(serializers.ModelSerializer):
    study_members = StudyMemberSerializer(source='studymember_set', many=True)

    class Meta:
        model = Study
        fields = ['study_members', ]
