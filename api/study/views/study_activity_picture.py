from drf_yasg.utils import swagger_auto_schema

from ..models import Study
from ..serializers.activity_picture_of_study_sz import Activity_pictureOfStudySerializer
from ...activity_picture.serializers.activity_picture_sz import ActivityPictureSerializer

from ...activity_picture.models import ActivityPicture

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


        """,
    )
    def get(self, request, *args, **kwargs):
        study_id = self.kwargs['studies_id']
        ap = ActivityPicture.objects.filter(study_id=study_id)
        serializer = ActivityPictureSerializer(ap, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=Activity_pictureOfStudySerializer,
        responses={201: Activity_pictureOfStudySerializer()},
        tags=['activity_pictures'],
        operation_description=
        """
        스터디의 활동사진 생성 API

        ---
            요청사양
                - study : study의 id
                - activity_picture : 이미지 업로드
        """,
    )
    def post(self, request, *args, **kwargs):
        serializer = ActivityPictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
