from rest_framework import serializers
from ..models import Study
from ...activity_picture.serializers import ActivityPictureSerializer


class Activity_pictureOfStudySerializer(serializers.ModelSerializer):
    study_activity_picture = ActivityPictureSerializer(source='activitypicture_set', many=True)

    class Meta:
        model = Study
        fields = ['study_activity_picture', ]
