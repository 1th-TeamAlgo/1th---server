from rest_framework import serializers
from .models import UserCategory

class UserCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCategory
        fields = ['user_category_id', 'user_id', 'category_id']


