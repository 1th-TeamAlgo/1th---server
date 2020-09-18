from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from ..models import Study
from ..serializers.study_detail_sz import StudyDetailSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


class StudyDetail(APIView):
    @swagger_auto_schema(
        responses={200: StudyDetailSerializer()},
        tags=['studies'],
        operation_description=
        """
        특정 id를 가진 스터디 그룹 조회 API

        """,
    )
    def get(self, request, *args, **kwargs):
        print("들어온다")
        print(self.kwargs['studies_id'])
        study = get_object_or_404(Study, pk=self.kwargs['studies_id'])
        serializer = StudyDetailSerializer(study)
        return Response(serializer.data)
