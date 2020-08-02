from django.shortcuts import get_object_or_404, redirect
from drf_yasg.utils import swagger_auto_schema

from .models import Study
from .serializers import StudySerializer, StudyDetailSerializer, StudyMemberSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class StudyList(APIView):
    @swagger_auto_schema(
        responses={200: StudySerializer(many=True)},
        tags=['studies'],
        operation_description=
        """
        스터디 그룹 조회 API
 
        """,
    )
    def get(self, request):
        get_data = request.query_params
        serializer = self.get_serializer(get_data=get_data)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=StudySerializer,
        responses={201: StudySerializer()},
        tags=['studies'],
        operation_description=
        """
        스터디 그룹 생성 API
        """,
    )
    def post(self, request):
        serializer = StudySerializer(data=request.data)
        if serializer.is_valid():
            # study = serializer.save(commit=False)
            # study.category = request.category
            # study.save()
            # return redirect(study)
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
    @swagger_auto_schema(
        responses={200: StudyDetailSerializer()},
        tags=['studies'],
        operation_description=
        """
        특정 id를 가진 스터디 그룹 조회 API
        
        """,
    )
    def get_object(self, pk):
        return get_object_or_404(Study, pk=pk)

    def get(self, request, pk):
        study_member = self.get_object(pk)
        serializer = StudyDetailSerializer(study_member)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudyMember(APIView):
    @swagger_auto_schema(
        responses={200: StudyMemberSerializer()},
        tags=['studies'],
        operation_description=
        """
        스터디 그룹의 특정 id를 가진 스터디 맴버 조회 API

        """,
    )
    def get_object(self, pk):
        return get_object_or_404(Study, pk=pk)

    def get(self, request, pk):
        study_member = self.get_object(pk)
        serializer = StudyMemberSerializer(study_member)
        return Response(serializer.data, status=status.HTTP_200_OK)
