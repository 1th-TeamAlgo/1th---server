from rest_framework import serializers
from .models import Study
from ..study_member.serializers import StudyMemberSerializer


class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ['study_id', 'category', 'title', 'limit', 'description', 'create_at', 'update_at', ]


class StudyDetailSerializer(serializers.ModelSerializer):
    study_members = StudyMemberSerializer(source='studymember_set', many=True, read_only=True)

    class Meta:
        model = Study
        fields = ['study_id', 'category_id', 'title', 'limit', 'description', 'create_at', 'update_at',
                  'study_members', ]


class StudyMemberSerializer(serializers.ModelSerializer):
    study_members = StudyMemberSerializer(source='studymember_set', many=True, read_only=True)

    class Meta:
        model = Study
        fields = ['study_members', ]
