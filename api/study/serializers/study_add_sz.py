from rest_framework import serializers
from ..models import Study


class StudyAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ['study_id', 'category', 'title', 'limit', 'description', 'study_image', ]
