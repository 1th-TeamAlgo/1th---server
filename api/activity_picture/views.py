from django.shortcuts import get_object_or_404
from .models import ActivityPicture
from .serializers import ActivityPictureSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class APList(APIView):
    def get(self, request):
        ap = ActivityPicture.objects.all()
        serializer = ActivityPictureSerializer(ap, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActivityPictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class APDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(ActivityPicture, pk=pk)

    def get(self, request, pk):
        ap = self.get_object(pk)
        serializer = ActivityPictureSerializer(ap)
        return Response(serializer.data, status=status.HTTP_200_OK)
