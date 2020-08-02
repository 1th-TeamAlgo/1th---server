from django.shortcuts import get_object_or_404
from .models import Study
from .serializers import StudySerializer, StudyDetailSerializer, StudyMemberSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class StudyList(APIView):
    def get(self, request):
        get_data = request.query_params
        serializer = self.get_serializer(get_data=get_data)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer(self, get_data):
        if 'title' in get_data:
            category = Study.objects.filter(title__contains=get_data['title'])
            serializer = StudySerializer(category, many=True)

        else:
            category = Study.objects.all()
            serializer = StudySerializer(category, many=True)

        return serializer


class StudyDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Study, pk=pk)

    def get(self, request, pk):
        study_member = self.get_object(pk)
        serializer = StudyDetailSerializer(study_member)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudyMember(APIView):
    def get_object(self, pk):
        return get_object_or_404(Study, pk=pk)

    def get(self, request, pk):
        study_member = self.get_object(pk)
        serializer = StudyMemberSerializer(study_member)
        return Response(serializer.data, status=status.HTTP_200_OK)
