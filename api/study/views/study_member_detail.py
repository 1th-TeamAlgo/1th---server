from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from ...study_member.serializers.study_member_sz import StudyMemberSerializer
from ...study_member.serializers.study_member_delete_sz import StudyMemberDeleteSerializer
from ...study_member.models import StudyMember

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



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
