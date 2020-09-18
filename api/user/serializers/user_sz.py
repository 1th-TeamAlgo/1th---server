from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'email', 'name', 'age', 'cellphone', 'gender', 'description', 'categories',
                  'kakao_profile_img', 's3_profile_img', 'img_flag', ]
