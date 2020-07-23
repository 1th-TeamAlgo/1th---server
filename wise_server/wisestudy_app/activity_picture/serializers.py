from rest_framework import serializers
from .models import ActivityPicture

class ActivityPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPicture
        fields = ['activity_picture_id', 'study_id', 'path', 'create_at', 'update_at']


