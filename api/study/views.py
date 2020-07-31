from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from .models import Study
from .serializers import StudySerializer
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

        ---
        스터디 그룹을 조회합니다.
        # 내용
            - study_id : 기본키(식별번호)
            - category_id : 카테고리 기본키 참조(외래키)
            - title : 스터디 그룹 이름
            - limit : 스터디 그룹 모집 최대인원
            - description : 스터디 그룹 간단소개
            - create_at : 스터디 그룹 생성날짜
            - update_at : 스터디 그룹 업데이트 날짜
        """,
    )
    def get(self, request):
        study = Study.objects.all()
        serializer = StudySerializer(study, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=StudySerializer,
        responses={200: StudySerializer(many=True)},
        tags=['studies'],
        operation_description=
        """
        스터디 그룹 생성 API

        ---
        스터디 그룹을 생성합니다.
        """,
    )
    def post(self, request):
        serializer = StudySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class StudyDetail(APIView):
    @swagger_auto_schema(
        responses={200: StudySerializer(many=True)},
        tags=['studies'],
        operation_description=
        """
        특정 id를 가진 스터디 그룹 조회 API

        ---
        스터디그룹을 조회합니다.
        # 내용
            - study_id : 기본키(식별번호)
            - category_id : 카테고리 기본키 참조(외래키)
            - title : 스터디 그룹 이름
            - limit : 스터디 그룹 모집 최대인원
            - description : 스터디 그룹 간단소개
            - create_at : 스터디 그룹 생성날짜
            - update_at : 스터디 그룹 업데이트 날짜
        """,
    )
    def get(self, request, pk):
        study_member = self.get_object(pk)
        serializer = StudySerializer(study_member)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # pk에 해당하는  POST 객체 반환
    def get_object(self, pk):
        return get_object_or_404(Study, pk=pk)