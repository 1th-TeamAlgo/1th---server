from django.shortcuts import get_object_or_404
from .models import StudyMember
from .serializers import StudyMemberSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class StudyMemberList(APIView):
    def get(self, request):
        study_member = StudyMember.object.all()
        serializer = StudyMemberSerializer(study_member, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudyMemberSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class StudyMemeberDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(StudyMember,pk = pk)

    def get(self,request, pk):
        study_member = self.get_object(pk)
        serializer = StudyMemberSerializer(study_member)
        return Response(serializer.data, status=status.HTTP_200_OK)
