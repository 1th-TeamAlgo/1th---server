from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from .models import ActivityPicture
from .serializers import ActivityPictureSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class APList(APIView):
    @swagger_auto_schema(
        responses={200: ActivityPictureSerializer(many=True)},
        tags=['activity_pictures'],
        operation_description=
        """
        활동사진 조회 API

        ---
        활동사진을 조회합니다.
        # 내용
            - activity_picture_id : 기본키(식별번호)
            - study_id : 스터디 기본키 참조 (외래키)
            - path : 활동사진 경로
            - create_at : 활동사진 생성 날짜
            - update_at : 활동사진 업데이트 날짜        
        """,
    )
    def get(self, request):
        ap = ActivityPicture.objects.all()
        serializer = ActivityPictureSerializer(ap, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ActivityPictureSerializer,
        responses={200: ActivityPictureSerializer(many=True)},
        tags=['activity_pictures'],
        operation_description=
        """
        활동사진 생성 API
        
        ---
        할동사진을 생성합니다.
        """,
    )
    def post(self, request):
        serializer = ActivityPictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class APDetail(APIView):
    @swagger_auto_schema(
        responses={200: ActivityPictureSerializer(many=True)},
        tags=['activity_pictures'],
        operation_description=
        """
        특정 id를 가진 활동사진 조회 API

        ---
        특정 id를 가진 활동사진을 조회합니다.
        # 내용
            - activity_picture_id : 기본키(식별번호)
            - study_id : 스터디 기본키 참조 (외래키)
            - path : 사진 경로
            - create_at : 생성 날짜
            - update_at : 업데이트 날짜
        """,
    )
    def get(self, request, pk):
        ap = self.get_object(pk)
        serializer = ActivityPictureSerializer(ap)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # pk에 해당하는  POST 객체 반환
    def get_object(self, pk):
        return get_object_or_404(ActivityPicture, pk=pk)
