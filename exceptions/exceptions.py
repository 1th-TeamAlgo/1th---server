from rest_framework.views import exception_handler

def no_kakao_access_token(exc,context):
    response = exception_handler(exc,context)

    if response is not None:
        response.data['code'] = 400
        response.data['status']= 'Not_Found'