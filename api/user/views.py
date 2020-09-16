from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from .models import User
from .serializers import UserDetailSerializer, UserScheduleSerializer

from ..schedule.models import Schedule
from ..schedule.serializers import ScheduleSerializer2
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


class UserScheduleList(APIView):
    def get(self, request):
        user_payload = jwt_get_payload(request)
        user = self.get_object(user_payload['user_id'])

        year, month, day = request.GET.get('choice_date').split('-')
        choice_schedules = list()


        for study in user.study_set.all():
            schedules = study.schedule_set.all()
            filter_schedules = schedules.filter(datetime__year=year,
                                                 datetime__month=month,
                                                 datetime__day=day,
                                                 ).values()

            for i, schedule in enumerate(filter_schedules):
                schedule['study_title'] = study.title
                choice_schedules.append(schedule)


        print(choice_schedules)
        return Response(data=choice_schedules, status=status.HTTP_200_OK)

    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)
