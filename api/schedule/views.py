from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Schedule
from .serializers import ScheduleSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getAllOrCreateSchedule(request):
    if request.method == 'GET':
        query_set = Schedule.objects.all()
        print(query_set)
        serializer = ScheduleSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False,  json_dumps_params={'ensure_ascii': False})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ScheduleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


#단건조회
@csrf_exempt
def getSchedule(request, id):

    schedule = Schedule.objects.get(schedule_id=id)

    if request.method == 'GET':
        serialized_data = ScheduleSerializer(schedule)
        return JsonResponse(serialized_data.data, safe=False, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer_data = ScheduleSerializer(schedule,data=data)
        if serializer_data.is_valid():
            serializer_data.save()
            return JsonResponse(serializer_data.data, status=201)
        return JsonResponse(serializer_data.errors, status=400)

    elif request.method == 'DELETE':
        schedule.delete()
        return HttpResponse(status=204)
