from django.shortcuts import get_object_or_404
from .models import Schedule
from .serializers import ScheduleSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


class ScheduleList(APIView):
    @swagger_auto_schema(
        responses={200: ScheduleSerializer(many=True)},
        tags=['schedules'],
        operation_description=
        """
        스케줄 조회 API
    
        """,
    )
    def get(self, request):
        schedule = Schedule.objects.all()
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ScheduleSerializer,
        responses={201: ScheduleSerializer()},
        tags=['schedules'],
        operation_description=
        """
        스케줄 생성 API

        """,
    )
    def post(self, request):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class ScheduleDetail(APIView):
    @swagger_auto_schema(
        responses={200: ScheduleSerializer()},
        tags=['schedules'],
        operation_description=
        """
        특정 id를 가진 스케줄 조회 API
        
        """,
    )
    def get(self, request, pk):
        schedule = self.get_object(pk)
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # pk에 해당하는  POST 객체 반환
    def get_object(self, pk):
        return get_object_or_404(Schedule, pk=pk)

