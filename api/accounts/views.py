import requests
import jwt

from drf_yasg.utils import swagger_auto_schema
from config.settings.secret import SECRET_KEY

from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

import json

class KakaoAccount(APIView):
    renderer_classes = [JSONRenderer]

    dummy_jwt = {
        "jwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ ... 3XirwWnsXXrq0c3PMhRLEz5mFqbz2S2r_QxEM2Q"
    }

    @swagger_auto_schema(
        responses={200: json.dumps(dummy_jwt)},
        tags=['jwt'],
        operation_description=
        """
        Kakao access token으로 jwt 발급

        """,
    )
    def get(self, request, format=None):
        access_token = request.META['HTTP_KAKAO_ACCESS_TOKEN']
        kakao_account = self.get_kakao_account(access_token=access_token)

        return Response(data=kakao_account)

    def get_kakao_account(self, access_token):
        user_profile_info_uri = "https://kapi.kakao.com/v2/user/me"
        print(user_profile_info_uri)
        user_profile_info_uri_data = requests.post(user_profile_info_uri,
                                                   headers={'Authorization': f"Bearer ${access_token}"})
        user_json_data = user_profile_info_uri_data.json()

        kakao_account = user_json_data['kakao_account']
        nickname = kakao_account['profile']['nickname']
        email = kakao_account['email']
        birthday = kakao_account['birthday']

        data = {
            "nickname": nickname,
            'email': email,
            'birthday': birthday
        }

        user_jwt = self.user_jwt(data)
        return user_jwt

    def user_jwt(self, data):
        jwt_token = jwt.encode(data, SECRET_KEY, algorithm='HS256').decode('utf-8')

        data = {
            "jwt": jwt_token
        }

        return data
