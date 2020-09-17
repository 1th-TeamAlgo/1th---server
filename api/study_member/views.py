from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from ..user.models import User
from ..study.models import Study
from .models import StudyMember
from .serializers import StudyMemberSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import json

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
class StudyJoin(APIView):

    ## 스터디 가입 리스트 확인 api
    def get(self, request, *args, **kwargs):
        user_payload = jwt_get_payload(request)
        user = get_object_or_404(User, pk=user_payload['user_id'])
        study_id = self.kwargs['studies_id']

        data = cache.get(study_id)

        if data is None:
            study_apply_list = []

        else:
            study_apply_dict = json.loads(data)
            study_apply_dict = study_apply_dict[str(study_id)]
            study_apply_list = [value for value in study_apply_dict.values()]

        return Response(data=study_apply_list)

    # 스터디에 가입 하기 신청 api
    def post(self, request, *args, **kwargs):
        user_payload = jwt_get_payload(request)
        user = get_object_or_404(User, pk=user_payload['user_id'])
        study_id = self.kwargs['studies_id']
        study = get_object_or_404(Study, pk=study_id)

        data = cache.get(study_id)

        if data is None:
            cache.set(study_id, self.get_user_data(user))

        #else:
        #    study_apply_dict = data[str(study_id)]
        #    print(study_apply_dict)

        return self.get_user_data(user)

    # pk에 해당하는  POST 객체 반환
    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)

    def get_user_data(self, user):
        user_data = dict(
            user_id=user.user_id,
            user_name=user.name,
            user_age=user.age,
            user_cellphone=user.cellphone,
            user_description=user.description,
            user_category=user.categories,
        )

        user_data = dict(
            user_id = user_data
        )
        return user_data

