from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from ..models import Study
from ..serializers.study_sz import StudySerializer
from ..serializers.study_add_sz import StudyAddSerializer

from ...study_member.serializers.study_add_study_member_sz import StudyAddStudyMemberSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from lib.user_data import jwt_get_payload


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
        ---
            request_params
                - title : 검색할 스터디의 이름
        """,
    )
    def get(self, request):
        get_data = request.query_params
        serializer = self.get_serializer(get_data=get_data)
        return Response(serializer.data)

    def get_serializer(self, get_data):
        if get_data.get('title') is not None:
            print("타이틀 있다")
            study = Study.objects.filter(title__contains=get_data['title'])
            serializer = StudySerializer(study, many=True)

        else:
            print("타이틀 없다")
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
            request_body
                - study_image : 스터디 이미지
                - category : 카테고리 이름
                - title : 스터디 이름
                - limit : 인원 제한
                - description : 스터디 소개
        """,
    )
    def post(self, request):
        user_payload = jwt_get_payload(request)
        request.data['study_members_count'] = 1
        serializer = StudyAddSerializer(data=request.data)
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
