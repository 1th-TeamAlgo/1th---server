from rest_framework import serializers
from .models import Study


class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ['study_id', 'category_id', 'title', 'limit', 'description', 'create_at' , 'update_at']
