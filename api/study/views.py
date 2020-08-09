from django.shortcuts import get_object_or_404, redirect
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import Study
from .serializers import StudySerializer, StudyDetailSerializer, MemberOfStudySerializer, ScheduleOfStudySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class StudyList(APIView):
    param_hello_hint = openapi.Parameter(
        'title',
        openapi.IN_QUERY,
        description='스터디 이름으로 검색',
        type=openapi.TYPE_STRING
    )

    @swagger_auto_schema(
        manual_parameters=[param_hello_hint],
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

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer(self, get_data):
        if 'title' in get_data:
            study = Study.objects.filter(title__contains=get_data['title'])
            serializer = StudySerializer(study, many=True)

        else:
            study = Study.objects.all()
            serializer = StudySerializer(study, many=True)

        return serializer

    @swagger_auto_schema(
        request_body=StudySerializer,
        responses={201: StudySerializer()},
        tags=['studies'],
        operation_description=
        """
        스터디 그룹 생성 API
        
        ---
            요청사양
                - category : 카테고리 번호
                - title : 스터디 이름
                - limit : 인원 제한
                - descriptions : 스터디 소개
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


class StudyDetail(APIView):
    @swagger_auto_schema(
        responses={200: StudyDetailSerializer()},
        tags=['studies'],
        operation_description=
        """
        특정 id를 가진 스터디 그룹 조회 API
        
        """,
    )
    def get(self, request, pk):
        study = self.get_object(pk)
        serializer = StudyDetailSerializer(study)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self, pk):
        return get_object_or_404(Study, pk=pk)

    # def get(self, request, pk):
    #     study_member = self.get_object(pk)
    #     serializer = StudyDetailSerializer(study_member)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class StudyMember(APIView):
    @swagger_auto_schema(
        responses={200: MemberOfStudySerializer()},
        tags=['studies'],
        operation_description=
        """
        스터디 그룹의 특정 id를 가진 스터디 맴버 조회 API

        """,
    )
    def get(self, request, pk):
        study_member = self.get_object(pk)
        serializer = MemberOfStudySerializer(study_member)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # pk에 해당하는  POST 객체 반환
    def get_object(self, pk):
        return get_object_or_404(Study, pk=pk)

    # def get(self, request, pk):
    #     study_member = self.get_object(pk)
    #     serializer = StudyMemberSerializer(study_member)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def get_object(self, pk):
    #     return get_object_or_404(Study, pk=pk)

    @swagger_auto_schema(
        request_body=MemberOfStudySerializer,
        responses={201: MemberOfStudySerializer()},
        tags=['studies'],
        operation_description=
        """
        스터디 회원 생성 API
        
        ---
            요청사양
                -is_manager : 운영진인지 아닌지 구분
                
                
        """,
    )
    def post(self, request):
        serializer = MemberOfStudySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class StudySchedule(APIView):
    @swagger_auto_schema(
        responses={200: ScheduleOfStudySerializer()},
        tags=['studies'],
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
    
    def get(self, request, pk):
        print("StudySchedule")
        study_schedule = self.get_object(pk)
        print(study_schedule)
        serializer = ScheduleOfStudySerializer(study_schedule)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self, pk):
        return get_object_or_404(Study, pk=pk)
