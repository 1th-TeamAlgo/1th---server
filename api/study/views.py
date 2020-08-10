from django.shortcuts import get_object_or_404, redirect
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import Study
from .serializers import StudySerializer, StudyDetailSerializer, MemberOfStudySerializer, ScheduleOfStudySerializer
from ..schedule.serializers import ScheduleSerializer, ScheduleDeleteSerializer
from ..schedule.models import Schedule
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
    def get(self, request, *args, **kwargs):
        study = self.get_object(self.kwargs['studies_id'])
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
    def get(self, request, *args, **kwargs):
        study_member = self.get_object(self.kwargs['studies_id'])
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
    def get(self, request, *args, **kwargs):
        print("StudySchedule")
        study_schedule = self.get_object(self.kwargs['studies_id'])
        print(study_schedule)
        serializer = ScheduleOfStudySerializer(study_schedule)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
                - datetime : 일정 날짜
                - place : 장소
                - address : 주소
                - title : 일정 이름
                - description : 일정 소개 

        """,
    )
    def post(self, request, *args, **kwargs):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        return get_object_or_404(Study, pk=pk)


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
        print("SADFSADFSDAFSDF")
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
            수정 가능한 필드 (
                - datetime : 스케쥴 날짜
                - place : 스케쥴 장소
                - address : 스케쥴 주소
                - title : 스케쥴 제목
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
