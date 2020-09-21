from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from ..models import ActivityPicture
from ..serializers.activity_picture_sz import ActivityPictureSerializer
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
                - activity_picture: image 파일 업로드
        """,
    )
    def post(self, request, *args, **kwargs):
        study_id = self.kwargs['stuies_id']

        serializer = ActivityPictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
