from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from .models import StudyMember
from .serializers import StudyMemberSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class StudyMemberList(APIView):
    @swagger_auto_schema(
        responses={200: StudyMemberSerializer(many=True)},
        tags=['study_members'],
        operation_description=
        """
        스터디 회원 조회 API

        ---
        스터디 회원을 조회합니다.
        
        """,
    )
    def get(self, request):
        study_member = StudyMember.objects.all()
        serializer = StudyMemberSerializer(study_member, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=StudyMemberSerializer,
        responses={200: StudyMemberSerializer(many=True)},
        tags=['study_members'],
        operation_description=
        """
        스터디 회원 생성 API

        ---
        스터디 회원을 생성합니다.
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
        responses={200: StudyMemberSerializer(many=True)},
        tags=['study_members'],
        operation_description=
        """
        특정 id를 가진 스터디 회원 조회 API

        ---
        스터디회원을 조회합니다.
        
        """,
    )
    def get(self, request, pk):
        study_member = self.get_object(pk)
        serializer = StudyMemberSerializer(study_member)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # pk에 해당하는  POST 객체 반환
    def get_object(self, pk):
        return get_object_or_404(StudyMember, pk=pk)
