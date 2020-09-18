from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from ...schedule.serializers.schedule_sz import ScheduleSerializer
from ...schedule.serializers.schedule_delete_sz import ScheduleDeleteSerializer

from ...schedule.models import Schedule

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

## --스케줄 디테일--
class StudyScheduleDetail(APIView):
    @swagger_auto_schema(
        responses={200: ScheduleSerializer()},
        tags=['schedules'],
        operation_description=
        """
        특정 id를 가진 스케줄 조회 API

        ---
            요청사항
                - schedule_id : 스케쥴 id
        """,
    )
    def get(self, request, *args, **kwargs):
        print("ScheduleDetail")
        schedule = self.get_object(schedule_id=self.kwargs['schedules_id'],
                                   study=self.kwargs['studies_id'])
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: ScheduleSerializer()},
        tags=['schedules'],
        operation_description=
        """
        특정 id를 가진 스케줄 수정 API

        ---       
            수정 가능한 필드 :
                - datetime : 스케쥴 날짜
                - place : 스케쥴 장소
                - description : 스케쥴 설명
        """,
    )
    def put(self, request, *args, **kwargs):
        schedule = self.get_object(schedule_id=self.kwargs['schedules_id'],
                                   study=self.kwargs['studies_id'])

        serializer = ScheduleSerializer(schedule, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @swagger_auto_schema(
        responses={200: ScheduleDeleteSerializer()},
        tags=['schedules'],
        operation_description=
        """
        특정 id를 가진 스케줄 삭제 API

        ---
            요청사항
                - schedule_id : 스케쥴 id
        """,
    )
    def delete(self, request, *args, **kwargs):
        schedule = self.get_object(schedule_id=self.kwargs['schedules_id'], study=self.kwargs['studies_id'])
        serializer = ScheduleDeleteSerializer(schedule)
        schedule.delete()
        return Response(data=serializer.data)

    # pk에 해당하는  POST 객체 반환
    def get_object(self, study, schedule_id):
        return get_object_or_404(Schedule, pk=schedule_id, study=study)


