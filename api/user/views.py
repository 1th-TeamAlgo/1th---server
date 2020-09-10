from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from .models import User
from .serializers import UserDetailSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from lib.user_data import jwt_get_payload


class UserList(APIView):
    @swagger_auto_schema(
        responses={200: UserDetailSerializer(many=True)},
        tags=['users'],
        operation_description=
        """
            회원 조회 API 
            
            - 회원의 JWT를 이용하여 회원의 정보를 조회 합니다.
        
        ---
        
            Header : x-jwt-token
        
        ---
        """,
    )
    def get(self, request):
        user_payload = jwt_get_payload(request)
        user = self.get_object(user_payload['user_id'])
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body=UserDetailSerializer,
        responses={201: UserDetailSerializer()},
        tags=['users'],
        operation_description=
        """
            특정 id를 가진 회원 수정 API (patch)
            patch 특성은 하나의 필드만 수정해도 가능하다는 것이다.
        
        ---
        
            kakao_profile_img 는 카카오의 프로필 사진의 링크 이고
        
            s3_profile_img 는 사용자가 직업 올린 프로필 사진의 링크 이다.
        
            구분을 위해서 img_flag를 추가 하였고 True면 kakao_profile을 사용중
        
            img_flag 가 False면 사용자가 직접 올린 사진을 사용하겠다는 뜻 이다.

        ---

        Header : x-jwt-token
    

        """,
    )
    def patch(self, request):
        user_payload = jwt_get_payload(request)
        user = self.get_object(user_payload['user_id'])

        serializer = UserDetailSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)

