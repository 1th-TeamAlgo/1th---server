from django.shortcuts import get_object_or_404
from .models import Schedule
from .serializers import ScheduleSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class ScheduleList(APIView):
    def get(self, request):
        schedule = Schedule.objects.all()
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class ScheduleDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Schedule, pk=pk)

    def get(self, request, pk):
        schedule = self.get_object(pk)
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data, status=status.HTTP_200_OK)
