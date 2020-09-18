from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from ..models import Study
from ..serializers.activity_picture_of_study_sz import Activity_pictureOfStudySerializer
from ...activity_picture.serializers import ActivityPictureSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class StudyActivity_pictures(APIView):
    @swagger_auto_schema(
        responses={200: Activity_pictureOfStudySerializer()},
        tags=['activity_pictures'],
        operation_description=
        """
        스터디의 activity_pictures 목록 API

        ---
            정렬사항 
                - datetime의 역순으로 정렬

            요청사항
                - study_id : 스터디의 id

        """,
    )
    def get(self, request, *args, **kwargs):
        print("Activity_picture")
        study_activity_picture = self.get_object(self.kwargs['studies_id'])
        print(study_activity_picture)
        serializer = Activity_pictureOfStudySerializer(study_activity_picture)
        print(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def get(self, request, pk):
    #     activity_pictures = self.get_object(pk)
    #     serializer = Activity_pictureOfStudySerializer(activity_pictures)
    #
    #     print(serializer)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # # pk에 해당하는  POST 객체 반환
    # def get_object(self, pk):
    #     return get_object_or_404(Study, pk=pk)

    @swagger_auto_schema(
        request_body=Activity_pictureOfStudySerializer,
        responses={201: Activity_pictureOfStudySerializer()},
        tags=['activity_pictures'],
        operation_description=
        """
        스터디의 활동사진 생성 API

        ---
            요청사양
                - study: 스터디 번호
                - path: 파일 경로
        """,
    )
    def post(self, request, *args, **kwargs):
        serializer = ActivityPictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        return get_object_or_404(Study, pk=pk)
    # def post(self, request, pk):
    #     # 1. URL path에 있는 아이디로 study 객체 조회
    #     study = self.get_object(pk)
    #     # 2. 요청 데이터에 맞는 모델로 변환할 수 있는 serializer를 사용
    #     # - ForignKey 설정해놓은 study 객체를 관계로 설정해주기 위해 파라미터에 조회된 study 객체 넘겨줌
    #     # - 1st param: 관계 설정된 study 객체
    #     # - 2nd param: 객체를 만들기 위한 JSON data
    #     serializer = Activity_picturesSerializer(study, data=request.data)
    #
    #     if serializer.is_valid():
    #         # 3. serializer가 JSON 값으로 객체를 만들면서 1st param으로 넘어온 study를 자동으로 연결
    #         instance = serializer.save()
    #         print(instance)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
