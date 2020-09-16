from django.shortcuts import get_object_or_404, redirect
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import Study
from .serializers import StudySerializer, StudyDetailSerializer, MemberOfStudySerializer, ScheduleOfStudySerializer, \
    Activity_pictureOfStudySerializer, StudyAddSerializer
from ..schedule.serializers import ScheduleSerializer, ScheduleDeleteSerializer
from ..schedule.models import Schedule
from ..activity_picture.serializers import ActivityPictureSerializer, ActivityPictureDeleteSerializer
from ..activity_picture.models import ActivityPicture
from ..study_member.serializers import StudyMemberSerializer, StudyMemberDeleteSerializer, StudyAddStudyMemberSerializer
from ..study_member.models import StudyMember

from ..user.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from lib.user_data import jwt_get_payload

import redis

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

        print(f"serializer -> {serializer}")
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
        request_body=StudyAddSerializer,
        responses={201: StudyAddSerializer()},
        tags=['studies'],
        operation_description=
        """
        스터디 그룹 생성 API
        
        ---
            요청사양
                - study_image : 스터디 이미지
                - category : 카테고리 이름
                - title : 스터디 이름
                - limit : 인원 제한
                - description : 스터디 소개
        """,
    )
    def post(self, request):
        user_payload = jwt_get_payload(request)
        print(user_payload)
        print(" ### request.data ### ")
        print(request.data)
        serializer = StudyAddSerializer(data=request.data)
        print(request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()

            study_member_data = {
                'study': serializer.data['study_id'],
                'user': user_payload['user_id'],
                'is_manager': True,
            }

            study_member_serializer = StudyAddStudyMemberSerializer(data=study_member_data)

            if study_member_serializer.is_valid():
                study_member_serializer.save()
                print(study_member_serializer.data)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudyDetail(APIView):
    @swagger_auto_schema(
        responses={200: StudyDetailSerializer()},
        tags=['studies'],
        operation_description=
        """
        특정 id를 가진 스터디 그룹 조회 API
        
        """,
    )
    # def get(self, request, pk):
    #     study = self.get_object(pk)
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


## --활동사진--
class StudyActivity_pictures(APIView):
    @swagger_auto_schema(
        responses={200: Activity_pictureOfStudySerializer()},
        tags=['activity_pictures'],
        operation_description=
        """
        스터디의 activity_pictures 목록 API
        
        ---
            정렬사항 
                - datetime의 역순으로 정렬
                
            요청사항
                - study_id : 스터디의 id

        """,
    )
    def get(self, request, *args, **kwargs):
        print("Activity_picture")
        study_activity_picture = self.get_object(self.kwargs['studies_id'])
        print(study_activity_picture)
        serializer = Activity_pictureOfStudySerializer(study_activity_picture)
        print(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def get(self, request, pk):
    #     activity_pictures = self.get_object(pk)
    #     serializer = Activity_pictureOfStudySerializer(activity_pictures)
    #
    #     print(serializer)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # # pk에 해당하는  POST 객체 반환
    # def get_object(self, pk):
    #     return get_object_or_404(Study, pk=pk)

    @swagger_auto_schema(
        request_body=Activity_pictureOfStudySerializer,
        responses={201: Activity_pictureOfStudySerializer()},
        tags=['activity_pictures'],
        operation_description=
        """
        스터디의 활동사진 생성 API

        ---
            요청사양
                - study: 스터디 번호
                - path: 파일 경로
        """,
    )
    def post(self, request, *args, **kwargs):
        serializer = ActivityPictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        return get_object_or_404(Study, pk=pk)
    # def post(self, request, pk):
    #     # 1. URL path에 있는 아이디로 study 객체 조회
    #     study = self.get_object(pk)
    #     # 2. 요청 데이터에 맞는 모델로 변환할 수 있는 serializer를 사용
    #     # - ForignKey 설정해놓은 study 객체를 관계로 설정해주기 위해 파라미터에 조회된 study 객체 넘겨줌
    #     # - 1st param: 관계 설정된 study 객체
    #     # - 2nd param: 객체를 만들기 위한 JSON data
    #     serializer = Activity_picturesSerializer(study, data=request.data)
    #
    #     if serializer.is_valid():
    #         # 3. serializer가 JSON 값으로 객체를 만들면서 1st param으로 넘어온 study를 자동으로 연결
    #         instance = serializer.save()
    #         print(instance)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


##--활동사진 디테일--
class StudyActivity_picturesDetail(APIView):
    @swagger_auto_schema(
        responses={200: ActivityPictureSerializer()},
        tags=['activity_pictures'],
        operation_description=
        """
        특정 id를 가진 활동사진 조회 API
        
        ---
            요청사항
                - activity_picture_id : 활동사진 id
        """,
    )
    def get(self, request, *args, **kwargs):
        print("StudyActivity_picturesDetail GETs")
        activity_picture = self.get_object(activity_picture_id=self.kwargs['activity_pictures_id'],
                                           study=self.kwargs['studies_id'])
        serializer = ActivityPictureSerializer(activity_picture)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: ActivityPictureSerializer()},
        tags=['activity_pictures'],
        operation_description=
        """
        특정 id를 가진 활동사진 수정 API
        
        ---
            수정 가능한 필드 :
                - path: 파일경로
                
        """,
    )
    def put(self, request, *args, **kwargs):
        activity_picture = self.get_object(activity_picture_id=self.kwargs['activity_pictures_id'],
                                           study=self.kwargs['studies_id'])

        serializer = ActivityPictureSerializer(activity_picture, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @swagger_auto_schema(
        responses={200: ActivityPictureDeleteSerializer()},
        tags=['activity_pictures'],
        operation_description=
        """
        특정 id를 가진 활동사진 삭제 API
        ---
            요청사항
                - study : 스터디 번호
                - path : 파일경로
        """,
    )
    def delete(self, request, *args, **kwargs):
        activity_picture = self.get_object(activity_picture_id=self.kwargs['activity_pictures_id'],
                                           study=self.kwargs['studies_id'])
        serializer = ActivityPictureDeleteSerializer(activity_picture)
        activity_picture.delete()
        return Response(data=serializer.data)

    # pk에 해당하는  POST 객체 반환
    def get_object(self, study, activity_picture_id):
        return get_object_or_404(ActivityPicture, pk=activity_picture_id, study=study)


## --스터디맴버--
class Study_StudyMember(APIView):
    @swagger_auto_schema(
        responses={200: MemberOfStudySerializer()},
        tags=['StudyMember'],
        operation_description=
        """
        스터디 그룹의 특정 id를 가진 스터디 회원 조회 API

        """,
    )
    def get(self, request, *args, **kwargs):
        study_member = self.get_object(self.kwargs['studies_id'])
        serializer = MemberOfStudySerializer(study_member)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=StudyMemberSerializer,
        responses={201: StudyMemberSerializer()},
        tags=['StudyMember'],
        operation_description=
        """
        
        스터디 회원 생성 API
        ---
            Header : x-jwt-token
        ---
        
        """,
    )
    def post(self, request, *args, **kwargs):
        user_payload = jwt_get_payload(request)

        study_member_data = {
            'user': user_payload['user_id'],
            'study': self.kwargs['studies_id']
        }
        serializer = StudyAddStudyMemberSerializer(data=study_member_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    # pk에 해당하는 POST 객체 반환
    def get_object(self, pk):
        return get_object_or_404(Study, pk=pk)


##-- 스터디맴버 디테일--
class Study_StudyMemberDetail(APIView):
    @swagger_auto_schema(
        responses={200: StudyMemberSerializer()},
        tags=['StudyMember'],
        operation_description=
        """
        특정 id를 가진 회원 조회 API
        
            
        """,
    )
    def get(self, request, *args, **kwargs):
        print("스터디d맴버 디테일 시작")
        study_member = self.get_object(study_member_id=self.kwargs['study_members_id'],
                                       study=self.kwargs['studies_id'])
        print(study_member)
        serializer = StudyMemberSerializer(study_member)
        print(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: StudyMemberSerializer()},
        tags=['StudyMember'],
        operation_description=
        """
        특정 id를 가진 회원 수정 API
        ---
            수정 가능한 필드 :
                - is_manager : 운영진인지 아닌지 구분
                
        """,
    )
    def put(self, request, *args, **kwargs):
        study_member = self.get_object(study_member_id=self.kwargs['study_members_id'],
                                       study=self.kwargs['studies_id'])

        serializer = StudyMemberSerializer(study_member, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @swagger_auto_schema(
        responses={200: StudyMemberDeleteSerializer()},
        tags=['StudyMember'],
        operation_description=
        """
        특정 id를 가진 회원 삭제 API
        ---
            요청사항
                - studymember_id : 스터디회원 id
        """,
    )
    def delete(self, request, *args, **kwargs):
        study_member = self.get_object(study_member_id=self.kwargs['study_members_id'], study=self.kwargs['studies_id'])
        serializer = StudyMemberDeleteSerializer(study_member)
        study_member.delete()
        return Response(data=serializer.data)

    # pk에 해당하는  POST 객체 반환
    def get_object(self, study, study_member_id):
        return get_object_or_404(StudyMember, pk=study_member_id, study=study)


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
                - datetime : 일정 날짜 YY-MM-DDTHH:MM
                - place : 장소
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

from django.core.cache import cache

class StudyJoin(APIView):
    ## 스터디 가입 리스트 확인 (api/v1/studies/1/joinmember)

    def get(self, request, *args, **kwargs):
        value = cache.get('hi')
        print(value)
        return Response(data = None)
