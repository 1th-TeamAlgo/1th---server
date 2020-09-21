from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from ...activity_picture.serializers.activity_picture_sz import ActivityPictureSerializer, \
    ActivityPictureDeleteSerializer

from ...activity_picture.models import ActivityPicture

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class StudyActivityPicturesDetail(APIView):
    @swagger_auto_schema(
        responses={200: ActivityPictureSerializer()},
        tags=['activity_pictures'],
        operation_description=
        """
        특정 id를 가진 활동사진 조회
        ---
        """,
    )
    def get(self, request, *args, **kwargs):
        ap = get_object_or_404(ActivityPicture, pk=self.kwargs['activity_pictures_id'])
        serializer = ActivityPictureSerializer(ap)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: ActivityPictureSerializer()},
        tags=['activity_pictures'],
        operation_description=
        """
        특정 id를 가진 활동사진 삭제
        ---

        """,
    )

    def delete(self, request, *args, **kwargs):
        ap = get_object_or_404(ActivityPicture, pk=self.kwargs['activity_pictures_id'])
        ap.delete()

        try:
            study_id = self.kwargs['studies_id']
            ap = ActivityPicture.objects.filter(study_id=study_id)
            serializer = ActivityPictureSerializer(ap, many=True)
            return Response(data=serializer.data)
        except AttributeError:
            return Response(data=[])


