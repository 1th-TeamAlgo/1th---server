from drf_yasg import openapi
from rest_framework import serializers
from .models import ActivityPicture
# from ..study.serializers import StudySerializer


class ActivityPictureSerializer(serializers.ModelSerializer):
    # study = StudySerializer(read_only=True)

    class Meta:
        model = ActivityPicture
        fields = ['activity_picture_id', 'study', 'path', ]


class ActivityPictureDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPicture
        fields = ['study', 'path', ]
