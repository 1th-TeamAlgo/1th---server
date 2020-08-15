from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from .models import User
from .serializers import UserSerializer, UserDetailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class UserList(APIView):
    @swagger_auto_schema(
        responses={200: UserSerializer(many=True)},
        tags=['users'],
        operation_description=
        """
        회원 조회 API

        """,
    )
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={201: UserSerializer()},
        tags=['users'],
        operation_description=
        """      
        회원 생성 API
        
        ---
            요청사양
                - email : 이메일
                - name : 이름
                - age : 나이
                - cellphone : 휴대폰 번호
                - gender : 성별
                - description : 소개
                - categories : 관심분야
        """,
    )
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
    @swagger_auto_schema(
        responses={200: UserDetailSerializer()},
        tags=['users'],
        operation_description=
        """
        특정 id를 가진 회원 조회 API
        
        """,
    )
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserDetailSerializer(user)
        print(serializer.data)
        return Response(serializer.data)

    # pk에 해당하는  POST 객체 반환
    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)

    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={201: UserSerializer()},
        tags=['users'],
        operation_description=
        """
        특정 id를 가진 회원 수정 API

        """,
    )
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        # request_body=UserSerializer,
        responses={200: '{"user_id": "1"}'},
        tags=['users'],
        operation_description=
        """
        특정 id를 가진 회원 삭제 API

        """,
    )
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_200_OK)
