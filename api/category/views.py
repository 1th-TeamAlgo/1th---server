from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import Category
from .serializers import CategorySerializer, CategoryDetailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Deprecate
class CategoryList(APIView):
    param_hello_hint = openapi.Parameter(
        'name',
        openapi.IN_QUERY,
        description='카테고리 이름으로 검색',
        type=openapi.TYPE_STRING
    )
    @swagger_auto_schema(
        manual_parameters=[param_hello_hint],
        responses={200: CategorySerializer(many=True)},
        tags=['categories'],
        operation_description=
        """
        카테고리 조회 API
    
        ---
        """,
    )
    def get(self, request):
        get_data = request.query_params
        serializer = self.get_serializer(get_data=get_data)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer(self, get_data):
        if 'name' in get_data:
            category = Category.objects.filter(name=get_data['name'])
            serializer = CategoryDetailSerializer(category, many=True)

        else:
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)

        return serializer

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request):
    #     get_data = request.query_params
    #
    #     serializer = self.get_serializer(get_data=get_data)
    #
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetail(APIView):
    @swagger_auto_schema(
        responses={200: CategoryDetailSerializer()},
        tags=['categories'],
        operation_description=
        """
        특정 id를 가진 카테고리 조회 API
        
        """,
    )
    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # pk에 해당하는  POST 객체 반환
    def get_object(self, pk):
        return get_object_or_404(Category, pk=pk)


