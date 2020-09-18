from .serializers import UserSignUpSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


class UserSignUp(APIView):
    # @swagger_auto_schema(
    #     request_body=UserSignUpSerializer,
    #     responses={201: UserSignUpSerializer()},
    #     tags=['users'],
    #     operation_description=
    #     """
    #     회원 생성 API
    #
    #     ---
    #         요청사양
    #             - name : 이름
    #             - age : 나이
    #             - cellphone : 휴대폰 번호
    #             - description : 자기소개
    #     """,
    # )
    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)