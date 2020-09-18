from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from ..models import User
from ...schedule.serializers.schedule_sz import ScheduleSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from lib.user_data import jwt_get_payload


class UserScheduleList(APIView):
    @swagger_auto_schema(
        responses={201: ScheduleSerializer()},
        tags=['users'],
        operation_description=
        """
            특정 날짜에 있는 나의 스터디 스케쥴 API

        ---
            Header : x-jwt-token
        ---
            query_params : choice_date = YYYY-MM-DD   


        """,
    )
    def get(self, request):
        user_payload = jwt_get_payload(request)
        user = self.get_object(user_payload['user_id'])

        year, month, day = request.GET.get('choice_date').split('-')
        choice_schedules = list()

        for study in user.study_set.all():
            schedules = study.schedule_set.all()
            filter_schedules = schedules.filter(datetime__year=year,
                                                datetime__month=month,
                                                datetime__day=day,
                                                ).values()

            for i, schedule in enumerate(filter_schedules):
                schedule['study_title'] = study.title
                choice_schedules.append(schedule)

        print(choice_schedules)
        return Response(data=choice_schedules, status=status.HTTP_200_OK)

    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)
