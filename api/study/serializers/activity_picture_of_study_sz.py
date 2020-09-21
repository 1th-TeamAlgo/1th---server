from rest_framework import serializers
from ...activity_picture.models import ActivityPicture


class Activity_pictureOfStudySerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityPicture
        fields = ['study', 'study_activity_picture',]
