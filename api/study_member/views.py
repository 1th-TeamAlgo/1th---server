from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from ..user.models import User
from ..study.models import Study
from .models import StudyMember
from .serializers import StudyMemberSerializer, StudyAddStudyMemberSerializer

from ..study.serializers import MemberOfStudySerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import json
import datetime

from lib.user_data import jwt_get_payload


class StudyMemberList(APIView):
    @swagger_auto_schema(
        responses={200: StudyMemberSerializer(many=True)},
        tags=['study_members'],
        operation_description=
        """
        스터디 회원 조회 API

        """,
    )
    def get(self, request):
        study_member = StudyMember.objects.all()
        serializer = StudyMemberSerializer(study_member, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=StudyMemberSerializer,
        responses={201: StudyMemberSerializer()},
        tags=['study_members'],
        operation_description=
        """
        스터디 회원 생성 API
        
        ---
            요청사양
                -is_manager : 운영진인지 아닌지 구분  
        """,
    )
    def post(self, request):
        serializer = StudyMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class StudyMemeberDetail(APIView):
    @swagger_auto_schema(
        responses={200: StudyMemberSerializer()},
        tags=['study_members'],
        operation_description=
        """
        특정 id를 가진 스터디 회원 조회 API

        """,
    )
    def get(self, request, pk):
        study_member = self.get_object(pk)
        serializer = StudyMemberSerializer(study_member)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # pk에 해당하는  POST 객체 반환
    def get_object(self, pk):
        return get_object_or_404(StudyMember, pk=pk)


from django.core.cache import cache


# /api/v1/studies/<int:studies_id>/members/apply
class StudyMemberJoin(APIView):
    def __init__(self):
        self.redis_data_expire_time = 25200

    ## 스터디 가입 리스트 확인 api
    @swagger_auto_schema(
        # responses={200},
        tags=['studies'],
        operation_description=
        """
        특정 id를 가진 스터디 회원 조회 API
        
        ---
            request_parmas : studies_id
        ---
        ```json
        response 
        {
            "code": 200,
            "status": "OK",
            "message": {
                "2": {
                    "user_id": 2,
                    "user_name": "김택윤",
                    "user_age": null,
                    "user_cellphone": null,
                    "user_description": null,
                    "user_category": null
                },
                "1": {
                    "user_id": 1,
                    "user_name": "이운기",
                    "user_age": 29,
                    "user_cellphone": "01086310498",
                    "user_description": "안드",
                    "user_category": null
                }
            }
        }
        ```
        """,
    )
    def get(self, request, *args, **kwargs):
        study_id = self.kwargs['studies_id']
        str_study_id = 'study:' + str(study_id)
        data = cache.get(str_study_id)

        if data is None:
            study_apply_list = []

        else:
            study_apply_list = cache.get(str_study_id)

        return Response(data=study_apply_list)

    # 스터디에 가입 하기 신청 api
    def post(self, request, *args, **kwargs):
        user_payload = jwt_get_payload(request)
        user = get_object_or_404(User, pk=user_payload['user_id'])
        study_id = self.kwargs['studies_id']
        str_study_id = self.str_study_id(study_id)

        if len(StudyMember.objects.filter(study_id=study_id, user_id=user_payload['user_id'])) > 0:
            return Response(data=["이미 들어있다"])

        apply_data = cache.get(str_study_id)

        if apply_data is None:
            print("if")
            cache.set(str_study_id, {user.user_id: self.get_user_data(user)}, self.redis_data_expire_time)

        else:
            print("else")
            study_apply_dict = apply_data
            study_apply_dict[user.user_id] = self.get_user_data(user)
            cache.set(str_study_id, study_apply_dict, self.redis_data_expire_time)

        apply_data = cache.get(str_study_id)

        return Response(data=apply_data)

    def get_user_data(self, user) -> dict:
        user_data = dict(
            user_id=user.user_id,
            user_name=user.name,
            user_age=user.age,
            user_cellphone=user.cellphone,
            user_description=user.description,
            user_category=user.categories,
        )

        return user_data

    def str_study_id(self, study_id):
        return 'study:' + str(study_id)

class StudyMemberConfirm(APIView):

    ## study 가입 신청 멤버 승인
    def post(self, request, *args, **kwargs):
        study_id = self.kwargs['studies_id']
        str_study_id = self.str_study_id(study_id)

        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, pk=user_id)

        self.apply_member_delete_redis(str_study_id, user_id)

        if len(StudyMember.objects.filter(study_id=study_id, user_id=user_id)) > 0:
            return Response(data=["이미 들어있다"])

        study_member_data = {
            'study': study_id,
            'user': user_id,
            'is_manager': False,
        }

        study_member_serializer = StudyAddStudyMemberSerializer(data=study_member_data)

        if study_member_serializer.is_valid():
            study_member_serializer.save()

        study_members = get_object_or_404(Study, pk=study_id)
        study_members_serializer = MemberOfStudySerializer(study_members)
        return Response(study_members_serializer.data)

    ## study 가입 신청 멤버 반려
    def delete(self, request, *args, **kwargs):
        study_id = self.kwargs['studies_id']
        str_study_id = self.str_study_id(study_id)

        user_id = request.POST.get('user_id')

        study_apply_dict = self.apply_member_delete_redis(str_study_id, user_id)

        return Response(data=study_apply_dict)

    ## 가입 승인 또는 반려 된 인원 redis에서 제거
    def apply_member_delete_redis(self, study_id, user_id):
        study_apply_dict = cache.get(study_id)

        if int(user_id) in study_apply_dict.keys():
            study_apply_dict.pop(int(user_id))
            cache.set(study_id, study_apply_dict)
            print(study_apply_dict)

        return study_apply_dict

    def str_study_id(self, study_id):
        return 'study:' + str(study_id)
