from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from .models import User
from .serializers import UserSerializer, UserDetailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from config.settings.secret import SECRET_KEY, ALGORITHM

import jwt


class UserList(APIView):
    @swagger_auto_schema(
        responses={200: UserSerializer(many=True)},
        tags=['users'],
        operation_description=
        """
        회원 조회 API
        
        ---
        
        Header : x-jwt-token
        """,
    )
    def get(self, request):
        user_payload = self.jwt_get_payload(request)
        pk = user_payload['user_id']
        user = self.get_object(pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={201: UserSerializer()},
        tags=['users'],
        operation_description=
        """
        특정 id를 가진 회원 수정 API
        
        ---
        
        Header : x-jwt-token

        """,
    )
    def put(self, request):
        user_payload = self.jwt_get_payload(request)
        pk = user_payload['user_id']
        user = self.get_object(pk)

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)

    def jwt_get_payload(self, request):
        user_jwt = request.META['HTTP_X_JWT_TOKEN']
        user_payload = jwt.decode(user_jwt, SECRET_KEY, algorithm=ALGORITHM)
        return user_payload

# class UserDetail(APIView):
#     @swagger_auto_schema(
#         responses={200: UserDetailSerializer()},
#         tags=['users'],
#         operation_description=
#         """
#         특정 id를 가진 회원 조회 API
#
#         """,
#     )
#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserDetailSerializer(user)
#         print(serializer.data)
#         return Response(serializer.data)
#
#     # pk에 해당하는  POST 객체 반환
#     def get_object(self, pk):
#         return get_object_or_404(User, pk=pk)
#
#     @swagger_auto_schema(
#         request_body=UserSerializer,
#         responses={201: UserSerializer()},
#         tags=['users'],
#         operation_description=
#         """
#         특정 id를 가진 회원 수정 API
#
#         """,
#     )
#     def put(self, request, pk):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     @swagger_auto_schema(
#         # request_body=UserSerializer,
#         responses={200: '{"user_id": "1"}'},
#         tags=['users'],
#         operation_description=
#         """
#         특정 id를 가진 회원 삭제 API
#
#         """,
#     )
#     def delete(self, request, pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_200_OK)
