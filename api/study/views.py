from django.shortcuts import get_object_or_404, redirect
from drf_yasg.utils import swagger_auto_schema

from .models import Study
from .serializers import StudySerializer, StudyDetailSerializer, StudyMemberSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class StudyList(APIView):
    @swagger_auto_schema(
        responses={200: StudySerializer(many=True)},
        tags=['studies'],
        operation_description=
        """
        ���͵� �׷� ��ȸ API
 
        """,
    )
    def get(self, request):
        study = Study.objects.all()
        serializer = StudySerializer(study, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=StudySerializer,
        responses={201: StudySerializer()},
        tags=['studies'],
        operation_description=
        """
        ���͵� �׷� ���� API

        ---
        ���͵� �׷��� �����մϴ�.
        """,
    )
    def post(self, request):
        serializer = StudySerializer(data=request.data)
        if serializer.is_valid():
            # study = serializer.save(commit=False)
            # study.category = request.category
            # study.save()
            # return redirect(study)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class StudyDetail(APIView):
    @swagger_auto_schema(
        responses={200: StudyDetailSerializer()},
        tags=['studies'],
        operation_description=
        """
        Ư�� id�� ���� ���͵� �׷� ��ȸ API

        ---
        ���͵�׷��� ��ȸ�մϴ�.
        
        """,
    )
    def get(self, request, pk):
        study_member = self.get_object(pk)
        serializer = StudyDetailSerializer(study_member)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudyMember(APIView):
    def get_object(self, pk):
        return get_object_or_404(Study, pk=pk)

    def get(self, request, pk):
        study_member = self.get_object(pk)
        serializer = StudyMemberSerializer(study_member)
        return Response(serializer.data, status=status.HTTP_200_OK)
