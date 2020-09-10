from rest_framework import serializers
from .models import TestImage

class TestImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestImage
        fields = '__all__'