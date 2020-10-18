from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import ActivityPicture
from .serializersasdf import ActivityPictureSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Deprecate
class APList(APIView):
    @swagger_auto_schema(
        responses={200: ActivityPictureSerializer(many=True)},
        tags=['activity_pictures'],
        operation_description=
        """
        활동사진 조회 API

        """,
    )
    def get(self, request, *args, **kwargs):
        study_id = self.kwargs['studies_id']
        ap = ActivityPicture.objects.filter(study_id=study_id)
        #ap = ActivityPicture.objects.all()
        serializer = ActivityPictureSerializer(ap,many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body=ActivityPictureSerializer,
        responses={201: ActivityPictureSerializer()},
        tags=['activity_pictures'],
        operation_description=
        """
        활동사진 생성 API
        
        ---
            요청사양
                - path: 파일 경로
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
        responses={200: ActivityPictureSerializer()},
        tags=['activity_pictures'],
        operation_description=
        """
        특정 id를 가진 활동사진 조회 API

        """,
    )
    def get(self, request, pk):
        ap = self.get_object(pk)
        serializer = ActivityPictureSerializer(ap)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # pk에 해당하는  POST 객체 반환
    def get_object(self, pk):
        return get_object_or_404(ActivityPicture, pk=pk)
