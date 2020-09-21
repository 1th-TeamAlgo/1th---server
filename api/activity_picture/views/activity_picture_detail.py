from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from ..models import ActivityPicture
from ..serializers.activity_picture_sz import ActivityPictureSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class APDetail(APIView):
    @swagger_auto_schema(
        responses={200: ActivityPictureSerializer()},
        tags=['activity_pictures'],
        operation_description=
        """
        특정 id를 가진 활동사진 조회 API

        """,
    )
    def get(self, request, *args, **kwargs):
        ap = get_object_or_404(ActivityPicture, pk=self.kwargs['activity_pictures_id'])
        serializer = ActivityPictureSerializer(ap)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        ap = get_object_or_404(ActivityPicture, pk=self.kwargs['activity_pictures_id'])
        ap.delete()

        return Response(data=[])
