from rest_framework.exceptions import ParseError
from config.settings.secret import SECRET_KEY, ALGORITHM
from rest_framework.response import Response
import jwt
import json
from django.http import HttpResponse, JsonResponse


class UserJwtCheckMiddleware:
    print("UserJWtCheckMiddleware 들어옴")
    METHOD = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')

    def __init__(self, get_response):
        self.get_response = get_response
        self.user_payload = dict()

    def __call__(self, request):
        print("jwt check")
        try:
            user_jwt = request.META['HTTP_X_JWT_TOKEN']
            print(user_jwt)
            self.user_payload = jwt.decode(user_jwt, SECRET_KEY, algorithm=ALGORITHM)
            print(self.user_payload)

            response = self.get_response(request)
            if hasattr(self, 'process_response'):
                response = self.process_response(request, response)
            return response

        except (KeyError, jwt.DecodeError):
            print("jwt 없다")
            return self.process_request(request, 'NO_JWT_TOKEN')

    def process_response(self, request, response):
        return response

    def process_request(self, request, error_type):
        if error_type == "NO_JWT_TOKEN":
            return JsonResponse(data=self.make_response(status=error_type, code=401))

    def make_response(self, status, code, message=[]):
        response_data = dict(
            code=code,
            status=status,
            message=[]
        )
        return response_data