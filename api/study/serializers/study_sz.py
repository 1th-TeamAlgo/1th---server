from rest_framework import serializers
from ..models import Study


class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ['study_id', 'category', 'title', 'study_members_count', 'limit', 'description', 'study_image', ]
