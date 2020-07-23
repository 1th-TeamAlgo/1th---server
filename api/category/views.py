from django.shortcuts import get_object_or_404
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class CategoryList(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    def get_object(self, pk):
        print("###########################")
        print(pk)
        return get_object_or_404(Category, pk)

    def get(self, request, pk, format=None):
        print("category get")
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

# @csrf_exempt
# def Category_list(request):
#     if request.method == 'GET':
#         query_set = Category.objects.all()
#         print(query_set)
#         serializer = CategorySerializer(query_set, many = True)
#         return JsonResponse(serializer.data, safe=False,  json_dumps_params={'ensure_ascii': False})
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = CategorySerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# #단건조회
# @csrf_exempt
# def getAllOrCreateCategory(request):
#     if request.method == 'GET':
#         query_set = Category.objects.all()
#         print(query_set)
#         serializer = CategorySerializer(query_set, many = True)
#         return JsonResponse(serializer.data, safe=False,  json_dumps_params={'ensure_ascii': False})
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = CategorySerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
#
# #단건조회
# @csrf_exempt
# def getCategory(request, id):
#
#     category = Category.objects.get(category_id=id)
#
#     if request.method == 'GET':
#         serialized_data = CategorySerializer(category)
#         return JsonResponse(serialized_data.data, safe=False, json_dumps_params={'ensure_ascii': False})
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer_data = CategorySerializer(category,data=data)
#         if serializer_data.is_valid():
#             serializer_data.save()
#             return JsonResponse(serializer_data.data, status=201)
#         return JsonResponse(serializer_data.errors, status=400)
#
#     elif request.method == 'DELETE':
#         category.delete()
#         return HttpResponse(status=204)
