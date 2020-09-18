from rest_framework import serializers
from ..models import Study
from ...schedule.serializers.schedule_sz import ScheduleSerializer


class ScheduleOfStudySerializer(serializers.ModelSerializer):
    study_schedule = ScheduleSerializer(source='schedule_set', many=True)

    class Meta:
        model = Study
        fields = ['study_schedule', ]
