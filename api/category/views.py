from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class CategoryList(APIView):
    @swagger_auto_schema(
        responses={200: CategorySerializer(many=True)},
        tags=['categories'],
        operation_description=
        """
        카테고리 조회 API
    
        ---
        카테고리를 조회합니다.
        # 내용
            - category_id : 기본키(식별번호)
            - name : 카테고리 이름
            - study : 스터디 그룹 정보
        """,
    )
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def post(self, request):
    #     serializer = CategorySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    @swagger_auto_schema(
        responses={200: CategorySerializer(many=True)},
        tags=['categories'],
        operation_description=
        """
        특정 id를 가진 카테고리 조회 API
        
        ---
        특정 id를 가진 카테고리를 조회합니다.
        # 내용
            - category_id : 기본키(식별번호)
            - name : 카테고리 이름
            - study : 스터디 그룹 정보
        """,
    )
    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # pk에 해당하는  POST 객체 반환
    def get_object(self, pk):
        return get_object_or_404(Category, pk=pk)



    # def put(self, request, pk):
    #     category = self.get_object(pk)
    #     serializer = CategorySerializer(category, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, pk):
    #     category = self.get_object(pk)
    #     category.delete()
    #     return Response(status=status.HTTP_202_ACCEPTED)
