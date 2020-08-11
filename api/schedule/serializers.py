from rest_framework import serializers
from .models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source='study.title')

    class Meta:
        model = Schedule
        fields = ['schedule_id', 'study', 'title', 'datetime', 'place', 'address', 'title', 'description']


class ScheduleDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['study', 'title', ]
