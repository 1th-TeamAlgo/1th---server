from rest_framework import serializers
from .models import Study
from ..study_member.serializers import StudyMemberSerializer


class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ['study_id', 'category', 'title', 'limit', 'description', ]


class StudyDetailSerializer(serializers.ModelSerializer):
    study_members = StudyMemberSerializer(source='studymember_set', many=True, read_only=True)
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Study
        fields = ['study_id', 'category', 'category_name', 'title', 'limit', 'description', 'study_members', ]

        # def get_category_name(self, obj):
        #     return obj.category_name.name


class MemberOfStudySerializer(serializers.ModelSerializer):
    study_members = StudyMemberSerializer(source='studymember_set', many=True, read_only=True)

    class Meta:
        model = Study
        fields = ['study_members', ]
