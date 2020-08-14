from rest_framework import serializers
from ..user.models import User


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ['name', 'age', 'cellphone']
