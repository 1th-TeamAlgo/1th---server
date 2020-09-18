from rest_framework import serializers
from ..models import Schedule


class ScheduleDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['study', 'title', ]
