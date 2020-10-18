from drf_yasg.utils import swagger_auto_schema

from ..models import StudyMember

from ..serializers.study_member_sz import StudyMemberSerializer

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
            Header : x-jwt-token
        ---
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
            Header : x-jwt-token
        ---
            request_body
                -is_manager : 운영진인지 아닌지 구분  
        """,
    )
    def post(self, request):
        serializer = StudyMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
