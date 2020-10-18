from rest_framework import serializers
from ..models import Study


class StudyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ['study_id', 'category', 'title', 'limit', 'study_members_count', 'description', 'study_image', ]
