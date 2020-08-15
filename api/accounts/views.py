from django.shortcuts import render, redirect
import requests
import jwt
from config.settings.secret import SECRET_KEY
from rest_framework.response import Response
from django.http import JsonResponse
from ..user.models import User

import json
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


# class KakaoLogin(SocialLoginView):
#     adapter_class = KakaoOAuth2Adapter
from ..user.serializers import UserSerializer


def index(request):
    print("##### Func -> index #####")
    return render(request, 'index.html', {})


def oauth(request):
    print("##### Func -> oauth #####")
    access_token = request.META['HTTP_KAKAO_ACCESS_TOKEN']
    # code -> authorize_code
    print('access_token = ' + str(access_token))

    print("##### 사용자 정보 얻어 보기 #####")
    user_profile_info_uri = "https://kapi.kakao.com/v2/user/me"
    print(user_profile_info_uri)
    print("##### 사용자 정보 얻기 위햇 POST 날려봄 #####")
    user_profile_info_uri_data = requests.post(user_profile_info_uri,
                                               headers={'Authorization': f"Bearer ${access_token}"})
    user_json_data = user_profile_info_uri_data.json()

    kakao_account = user_json_data['kakao_account']

    email = kakao_account['email']
    gender = kakao_account['gender']

    data2 = {
        'email': email,
        'gender': gender,
    }
    print(data2)

    # kakao_account = user_json_data['kakao_account']
    nickname = kakao_account['profile']['nickname']
    email = kakao_account['email']
    birthday = kakao_account['birthday']
    data = {
        "nickname": nickname,
        'email': email,
        'birthday': birthday
    }
    print(data)

    user_jwt(data)
    data = {
        'jwt' : user_jwt(data)
    }
    return JsonResponse(data)

def user_jwt(data):
    jwt_token = jwt.encode(data,SECRET_KEY,algorithm='HS256')
    print("jwt토큰")
    print(jwt_token)
    print("jwt토큰 decode")
    jwt_token_str = jwt_token.decode('utf-8')
    print(jwt_token_str)
    return jwt_token_str



# def kakao_login(request):
#     print("##### Func -> kakao_login #####")
#     # GET /oauth/authorize?client_id={app_key}&redirect_uri={redirect_uri}&response_type=code HTTP/1.1
#     # Host: kauth.kakao.com
#
#     host = "https://kauth.kakao.com"
#     login_request_uri = host + "/oauth/authorize?"
#
#     client_id = 'be8d497f71f0e2427a73ffe6a8b93b9d'
#     redirect_uri = 'http://127.0.0.1:8000/oauth'
#
#     login_request_uri += 'client_id=' + client_id
#     login_request_uri += '&redirect_uri=' + redirect_uri
#     login_request_uri += '&response_type=code'
#
#     print("##### login_request_uri #####")
#     print(login_request_uri)
#     return redirect(login_request_uri)
#
#
# def kakao_logout(reuqest):
#     return redirect("https://naver.com")
