from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

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

class StudyJoin(APIView):
    ## 스터디 가입 리스트 확인 (api/v1/studies/1/joinmember)

    def get(self, request, *args, **kwargs):
        user_payload = jwt_get_payload(request)
        user = self.get_object(user_payload['user_id'])
        study_id = self.kwargs['studies_id']

        print("들어왔다")
        dataDict = {
            "key1": "테스트값1",
            "key2": "테스트값2",
            "key3": "테스트값3"
        }
        jsonDataDict = json.dumps(dataDict, ensure_ascii=False).encode('utf-8')

        cache.set("dict",jsonDataDict)
        cache.set
        # 데이터 get
        resultData = cache.get("dict")
        resultData = resultData.decode('utf-8')

        # json loads
        result = dict(json.loads(resultData))

        print(result)
        return Response(data = None)

    # pk에 해당하는  POST 객체 반환
    def get_object(self, pk):
        return get_object_or_404(StudyMember, pk=pk)