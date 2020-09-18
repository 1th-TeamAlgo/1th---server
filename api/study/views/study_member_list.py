from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from ..models import Study
from ..serializers.member_of_study_sz import MemberOfStudySerializer

from ...study_member.serializers.study_member_sz import StudyMemberSerializer
from ...study_member.serializers.study_add_study_member_sz import StudyAddStudyMemberSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from lib.user_data import jwt_get_payload


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
