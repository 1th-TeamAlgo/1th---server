from django.shortcuts import get_object_or_404
from .models import Category
from .serializers import CategorySerializer, CategoryDetailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class CategoryList(APIView):

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


class CategoryDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Category, pk=pk)

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategoryDetailSerializer(category)

        return Response(serializer.data, status=status.HTTP_200_OK)
