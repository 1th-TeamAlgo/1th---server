from rest_framework.exceptions import ParseError
from config.settings.secret import SECRET_KEY, ALGORITHM
import jwt

class UserJwtCheckMiddleware:
    print("UserJWtCheckMiddleware 들어옴")
    METHOD = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')


    def __init__(self, get_response):
        self.get_response = get_response
        self.user_payload = dict()

    def __call__(self, request):
        try:
            user_jwt = request.META['HTTP_X_JWT_TOKEN']
            self.user_payload = jwt.decode(user_jwt, SECRET_KEY, algorithm=ALGORITHM)
            print(self.user_payload)

        except (KeyError, jwt.DecodeError):
            return self.process_request(request, 'NO_JWT_TOKEN')

        finally:
            response = self.get_response(request)
            if hasattr(self, 'process_response'):
                response = self.process_response(request, response)
            return response

    def process_response(self,request,response):
        return response

    def process_request(self, request, error_type):
        if error_type == "NO_JWT_TOKEN":
            raise ParseError(detail="NO_JWT_TOKEN")


