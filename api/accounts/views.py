import requests
import jwt

from drf_yasg.utils import swagger_auto_schema
from config.settings.secret import SECRET_KEY, ALGORITHM

from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

import json
from ..user.models import User
from ..user.serializers import UserSerializer


class KakaoAccount(APIView):
    renderer_classes = [JSONRenderer]

    dummy_jwt = {
        "code": 200,

        "status": "OK",

        "message": {

            "jwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ ... 3XirwWnsXXrq0c3PMhRLEz5mFqbz2S2r_QxEM2Q",
        }
    }

    @swagger_auto_schema(
        responses={200: json.dumps(dummy_jwt)},
        tags=['jwt'],
        operation_description=
        """
        Kakao access token으로 jwt 발급
        
        ---
        
        Header : kakao-access-token
        """,
    )
    def get(self, request, format=None):
        print("############ GET ############")
        access_token = request.META['HTTP_KAKAO_ACCESS_TOKEN']
        kakao_account = self.get_kakao_account(access_token=access_token)

        return Response(data=kakao_account)

    def get_kakao_account(self, access_token):
        print("############ get_kakao_account ############")
        user_profile_info_uri = "https://kapi.kakao.com/v2/user/me"
        print(user_profile_info_uri)
        user_profile_info_uri_data = requests.post(user_profile_info_uri,
                                                   headers={'Authorization': f"Bearer ${access_token}"})
        user_json_data = user_profile_info_uri_data.json()
        print(user_json_data)

        new_user_payload = self.make_payload(user_json_data)

        return new_user_payload

    def make_payload(self, user_json_data):
        print("############ make_payload ############")
        ## jwt를 발급 받는다는것은 현재 스터디에 가입이 안되있다는것
        ## 그래서 바로 기본적인 user의 model을 만들어 주고
        ## 안드로이드에서 추가적인 데이터를 입력받도록 진행한다고 함.

        ### jwt 생성 부분 ###

        kakao_account = user_json_data['kakao_account']
        nickname = kakao_account['profile']['nickname']
        email = kakao_account['email']
        kakao_profile_img = kakao_account['profile']['profile_image_url']
        is_user = User.objects.filter(email=email)
        is_user_len = len(is_user)

        print("IF 들어가기전")
        if len(is_user) == 0:
            ### 새로운 user model 생성 부분 ###
            print("새로운 user model")

            new_user = User(name=nickname, email=email, profile_img=kakao_profile_img)
            new_user.save()
            user_serailizer = UserSerializer(new_user)

        else:
            ### 기존 user model ###
            print("기존 user model")

            is_user = is_user.values()
            print(is_user)
            user_serailizer = UserSerializer(is_user[0])
            print(user_serailizer.data)

        data = {
            'user_id': user_serailizer.data['user_id'],
            "nickname": nickname,
            'email': email,
        }

        jwt_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM).decode('utf-8')

        data = {
            "jwt": jwt_token,
            # "user": user_serailizer.data
        }

        return data
