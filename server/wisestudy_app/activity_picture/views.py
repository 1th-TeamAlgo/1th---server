from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ActivityPicture
from .serializers import ActivityPictureSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

#전체조회
@csrf_exempt
def getAllOrCreateActivityPicture(request):
    if request.method == 'GET':
        query_set = ActivityPicture.objects.all()
        print(query_set)
        serializer = ActivityPictureSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False,  json_dumps_params={'ensure_ascii': False})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ActivityPictureSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


#단건조회
@csrf_exempt
def getActivityPicture(request, id):

    activity_picture = ActivityPicture.objects.get(activity_picture_id=id)

    if request.method == 'GET':
        serialized_data = ActivityPictureSerializer(activity_picture)
        return JsonResponse(serialized_data.data, safe=False, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer_data = ActivityPictureSerializer(activity_picture,data=data)
        if serializer_data.is_valid():
            serializer_data.save()
            return JsonResponse(serializer_data.data, status=201)
        return JsonResponse(serializer_data.errors, status=400)

    elif request.method == 'DELETE':
        activity_picture.delete()
        return HttpResponse(status=204)





