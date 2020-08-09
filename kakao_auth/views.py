from django.shortcuts import get_object_or_404, redirect
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import requests


class KakaoGetCode(APIView):

    def get(self, request):
        json_data = self.get_token(request)

        # access_token = json_data['access_token']
        #
        # print(type(json_data))
        # for key, value in json_data.items():
        #     print("key -> {} \n value -> {}".format(key, value))
        # print("##### access_token #####")
        # print(access_token)
        #
        # print("##### 사용자 정보 얻어 보기 #####")
        # user_profile_info_uri = "https://kapi.kakao.com/v2/user/me"
        # print(user_profile_info_uri)
        #
        # print("##### 사용자 정보 얻기 위햇 POST 날려봄 #####")
        # user_profile_info_uri_data = requests.post(user_profile_info_uri,
        #                                            headers={'Authorization': f"Bearer ${access_token}"})
        # user_json_data = user_profile_info_uri_data.json()
        #
        # for key, value in user_json_data.items():
        #     print(f"key -> {key} \n value -> {value}")
        # for key, value in user_json_data["kakao_account"].items():
        #     print(f"key -> {key} \n value -> {value}")
        # return redirect('index')

        # return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(data=None)

    def get_token(self, request):
        get_code = request.META['HTTP_KAKAO_CODE']
        # serializer = self.get_serializer(get_data=get_data)
        print("KAKAO HIHI")
        print(get_code)

        client_id = "be8d497f71f0e2427a73ffe6a8b93b9d"
        redirect_uri = 'http://127.0.0.1:8000/api/v1/auth/token'

        access_token_request_uri = "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"
        access_token_request_uri += "client_id=" + client_id
        access_token_request_uri += "&redirect_uri=" + redirect_uri
        access_token_request_uri += "&code=" + get_code

        print("##### access_token_request_uri #####")
        print(access_token_request_uri)

        access_token_request_uri_data = requests.get(access_token_request_uri)
        print("##### access_token #####")
        print(access_token_request_uri_data)
        json_data = access_token_request_uri_data.json()

        print("##### json_data #####")
        print(json_data)

        return json_data
