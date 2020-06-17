from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserCategory
from .serializers import UserCategorySerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getAllOrCreateUserCategory(request):
    if request.method == 'GET':
        query_set = UserCategory.objects.all()
        print(query_set)
        serializer = UserCategorySerializer(query_set, many = True)
        return JsonResponse(serializer.data, safe=False,  json_dumps_params={'ensure_ascii': False})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


#단건조회
@csrf_exempt
def getUserCategory(request, id):

    user_category = UserCategory.objects.get(user_category_id=id)

    if request.method == 'GET':
        serialized_data = UserCategorySerializer(user_category)
        return JsonResponse(serialized_data.data, safe=False, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer_data = UserCategorySerializer(user_category,data=data)
        if serializer_data.is_valid():
            serializer_data.save()
            return JsonResponse(serializer_data.data, status=201)
        return JsonResponse(serializer_data.errors, status=400)

    elif request.method == 'DELETE':
        user_category.delete()
        return HttpResponse(status=204)
