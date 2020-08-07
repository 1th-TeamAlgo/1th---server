from rest_framework import serializers
from .models import StudyMember


class StudyMemberSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='user.user_id')
    name = serializers.ReadOnlyField(source='user.name')
    email = serializers.ReadOnlyField(source='user.email')
    age = serializers.ReadOnlyField(source='user.age')
    cellphone = serializers.ReadOnlyField(source='user.cellphone')
    gender = serializers.ReadOnlyField(source='user.gender')
    categories = serializers.ReadOnlyField(source='user.categories')

    class Meta:
        model = StudyMember
        fields = ['is_manager', 'id', 'name', 'email', 'age', 'cellphone', 'gender', 'categories', ]
