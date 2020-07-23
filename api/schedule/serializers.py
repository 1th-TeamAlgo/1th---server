from rest_framework import serializers
from .models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['schedule_id', 'study_id', 'datetime', 'place', 'address', 'title', 'description']


