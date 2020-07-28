from rest_framework import serializers
from .models import Category
from ..study.serializers import StudySerializer


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    study = StudySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_id', 'name', 'study',]
