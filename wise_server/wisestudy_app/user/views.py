from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def options(self, request, *args, **kwargs):
        if self.metadata_class is None:
            return self.http_method_not_allowed(request, *args, **kwargs)

        data = self.metadata_class().determine_metadata(request, self)
        return Response({'a': 'a'}, status=status.HTTP_200_OK)


class UserDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

# #단건조회
# @csrf_exempt
# def getUser(request, id):
#
#     user = User.objects.get(user_id=id)
#
#     if request.method == 'GET':
#         serialized_data = UserSerializer(user)
#         return JsonResponse(serialized_data.data, safe=False, json_dumps_params={'ensure_ascii': False})
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer_data = UserSerializer(user,data=data)
#         if serializer_data.is_valid():
#             serializer_data.save()
#             return JsonResponse(serializer_data.data, status=201)
#         return JsonResponse(serializer_data.errors, status=400)
#
#     elif request.method == 'DELETE':
#         user.delete()
#         return HttpResponse(status=204)
