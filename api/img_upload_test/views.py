from .models import TestImage
from .serializers import TestImageSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class TestImageList(APIView):
    def get(self,request):
        test_image = TestImage.objects.all()
        serializer = TestImageSerializer(test_image, many=True)
        return Response(serializer.data)
        pass

    def post(self,request):
        print("Post 들어왔다")
        serializer = TestImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)