from django.shortcuts import get_object_or_404
from .models import Category
from .serializers import CategorySerializer, CategoryDetailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class CategoryList(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Category, pk=pk)

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategoryDetailSerializer(category)

        return Response(serializer.data, status=status.HTTP_200_OK)
