from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from ...user.models import User
from ..models import StudyMember

from rest_framework.response import Response
from rest_framework.views import APIView

from lib.user_data import jwt_get_payload

from django.core.cache import cache


# /api/v1/studies/<int:studies_id>/members/apply
class StudyMemberApply(APIView):
    def __init__(self):
        self.redis_data_expire_time = 25200

    ## 스터디 가입 리스트 확인 api
    @swagger_auto_schema(
        # responses={200},
        tags=['studies'],
        operation_description=
        """
        스터디에 가입 신청한 인원 리스트 확인    
        ---
            Header : x-jwt-token
        ---
            request_parmas
                - studies_id : 리스트 확인할 스터디의 id
        ---
        ```json
        response 
        {
            "code": 200,
            "status": "OK",
            "message": {
                "2": {
                    "user_id": 2,
                    "user_name": "김택윤",
                    "user_age": null,
                    "user_cellphone": null,
                    "user_description": null,
                    "user_category": null
                },
                "1": {
                    "user_id": 1,
                    "user_name": "이운기",
                    "user_age": 29,
                    "user_cellphone": "01086310498",
                    "user_description": "안드",
                    "user_category": null
                }
            }
        }
        ```
        """,
    )
    def get(self, request, *args, **kwargs):
        study_id = self.kwargs['studies_id']
        str_study_id = 'study:' + str(study_id)
        data = cache.get(str_study_id)

        if data is None:
            study_apply_list = []

        else:
            study_apply_list = cache.get(str_study_id)

        return Response(data=study_apply_list)

    @swagger_auto_schema(
        tags=['studies'],
        operation_description=
        """
        스터디에 가입 신청 하기 
        ---
            Header : x-jwt-token
        ---
            request_body
                - user_id : 스터디 가입 신청할 유저 id
        """,
    )

    # 스터디에 가입 하기 신청 api
    def post(self, request, *args, **kwargs):
        user_payload = jwt_get_payload(request)
        user = get_object_or_404(User, pk=user_payload['user_id'])
        study_id = self.kwargs['studies_id']
        str_study_id = self.str_study_id(study_id)

        if len(StudyMember.objects.filter(study_id=study_id, user_id=user_payload['user_id'])) > 0:
            return Response(data=["이미 들어있다"])

        apply_data = cache.get(str_study_id)

        if apply_data is None:
            print("if")
            cache.set(str_study_id, {user.user_id: self.get_user_data(user)}, self.redis_data_expire_time)

        else:
            print("else")
            study_apply_dict = apply_data
            study_apply_dict[user.user_id] = self.get_user_data(user)
            cache.set(str_study_id, study_apply_dict, self.redis_data_expire_time)

        apply_data = cache.get(str_study_id)

        return Response(data=apply_data)

    def get_user_data(self, user) -> dict:
        user_data = dict(
            user_id=user.user_id,
            user_name=user.name,
            user_age=user.age,
            user_cellphone=user.cellphone,
            user_description=user.description,
            user_category=user.categories,
        )

        return user_data

    def str_study_id(self, study_id):
        return 'study:' + str(study_id)
