from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from ..models import StudyMember
from ..serializers.study_member_sz import StudyMemberSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class StudyMemeberDetail(APIView):
    @swagger_auto_schema(
        responses={200: StudyMemberSerializer()},
        tags=['study_members'],
        operation_description=
        """
        특정 id를 가진 스터디 회원 조회 API
        ---
            Header : x-jwt-token
        ---
        """,
    )
    def get(self, request, pk):
        study_member = self.get_object(pk)
        serializer = StudyMemberSerializer(study_member)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # pk에 해당하는  POST 객체 반환
    def get_object(self, pk):
        return get_object_or_404(StudyMember, pk=pk)
