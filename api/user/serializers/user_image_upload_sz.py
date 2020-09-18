from rest_framework import serializers
from ..models import User


class UserImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['s3_profile_img', 'img_flag']
