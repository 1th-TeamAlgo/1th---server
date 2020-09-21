from drf_yasg import openapi
from rest_framework import serializers
from .models import ActivityPicture


class ActivityPictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityPicture
        fields = '__all__'


class ActivityPictureDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPicture
        fields = '__all__'
