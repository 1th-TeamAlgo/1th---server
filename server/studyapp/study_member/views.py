from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StudyMember
from .serializers import StudyMemberSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getAllOrCreateStudyMember(request):
    if request.method == 'GET':
        query_set = StudyMember.objects.all()
        print(query_set)
        serializer = StudyMemberSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False,  json_dumps_params={'ensure_ascii': False})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudyMemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


#단건조회
@csrf_exempt
def getStudyMember(request, id):

    study_member = StudyMember.objects.get(study_member_id=id)

    if request.method == 'GET':
        serialized_data = StudyMemberSerializer(study_member)
        return JsonResponse(serialized_data.data, safe=False, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer_data = StudyMemberSerializer(study_member,data=data)
        if serializer_data.is_valid():
            serializer_data.save()
            return JsonResponse(serializer_data.data, status=201)
        return JsonResponse(serializer_data.errors, status=400)

    elif request.method == 'DELETE':
        study_member.delete()
        return HttpResponse(status=204)
