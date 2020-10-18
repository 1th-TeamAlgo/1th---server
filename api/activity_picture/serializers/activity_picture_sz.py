from drf_yasg import openapi
from rest_framework import serializers
from ..models import ActivityPicture


class ActivityPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPicture
        fields = ['study', 'activity_picture_id', 'activity_picture', 'create_at', 'update_at', ]


class ActivityPictureDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPicture
        fields = '__all__'
