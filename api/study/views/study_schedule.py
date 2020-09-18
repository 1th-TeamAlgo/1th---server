from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from ..models import Study
from ..serializers.schedule_of_study_sz import ScheduleOfStudySerializer

from ...schedule.serializers.schedule_sz import ScheduleSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


## ---스케줄---
class StudySchedule(APIView):
    @swagger_auto_schema(
        responses={200: ScheduleOfStudySerializer()},
        tags=['schedules'],
        operation_description=
        """
        스터디의 schedule 목록

        ---
            정렬사항 
                - datetime의 역순으로 정렬

            요청사항
                - study_id : 스터디의 id
        """,
    )
    def get(self, request, *args, **kwargs):
        print("StudySchedule")
        study_schedule = self.get_object(self.kwargs['studies_id'])
        print(study_schedule)
        serializer = ScheduleOfStudySerializer(study_schedule)
        print(serializer)
        return Response(data=serializer.data)

    @swagger_auto_schema(
        request_body=ScheduleSerializer,
        responses={201: ScheduleSerializer()},
        tags=['schedules'],
        operation_description=
        """
        스케줄 생성 API

        ---
            요청사양
                - study : 스터디 id
                - datetime : 일정 날짜 YY-MM-DDTHH:MM
                - place : 장소
                - description : 일정 소개 
        """,
    )
    def post(self, request, *args, **kwargs):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.error)

    def get_object(self, pk):
        return get_object_or_404(Study, pk=pk)
