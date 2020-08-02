from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from .models import Category
from .serializers import CategorySerializer, CategoryDetailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class CategoryList(APIView):
    @swagger_auto_schema(
        responses={200: CategorySerializer(many=True)},
        tags=['categories'],
        operation_description=
        """
        List all categoies
    
        ---
        

        """,
    )
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetail(APIView):
    @swagger_auto_schema(
        responses={200: CategoryDetailSerializer()},
        tags=['categories'],
        operation_description=
        """
        GET a category
        
        """,
    )
    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # pk에 해당하는  POST 객체 반환
    def get_object(self, pk):
        return get_object_or_404(Category, pk=pk)


