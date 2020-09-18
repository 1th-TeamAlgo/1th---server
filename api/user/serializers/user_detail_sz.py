from rest_framework import serializers
from ..models import User
from .user_study_sz import UserStudySerializer


class UserDetailSerializer(serializers.ModelSerializer):
    '''
        UserList - patch
    '''
    study_list = UserStudySerializer(source='studymember_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'email', 'name', 'age', 'cellphone', 'gender', 'description', 'categories', 'study_list',
                  'kakao_profile_img', 's3_profile_img', 'img_flag', ]

        read_only_fields = ['user_id', 'email', ]
