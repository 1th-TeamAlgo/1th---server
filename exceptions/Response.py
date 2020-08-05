import json
from django.shortcuts import HttpResponse


class Response:
    RESPONSE_STATUS = {
        'OK': 200,
        'CREATE': 201,
        'ACCEPTED': 202,

        'BAD_REQUEST': 400,
        'UNAUTHORIZED': 401,
        'FORBIDDEN': 403,
        'NOT_FOUND': 404,

        'INTERNAL_SERVER_ERROR': 500,
        'SERVICE_UNAVAILABLE': 503,
        'GATEWAY_TIMEOUT': 504,

    }

    RESPONSE_CODE = {
        'OK': 0  # 정상
    }

    def Response(self, status='NORMAL', code='NORMAL', data=None):
        '''
        :param status: 상태
        :param code: 코드
        :param data: 데이터
        :return: django.shortcuts. HttpResponse
        '''

        content = dict()
        content['status'] = self.RESPONSE_STATUS[status]
        content['code'] = self.RESPONSE_CODE[status]

        if data:
            content['data'] = data

        self.HttpResponse = HttpResponse(content=json.dumps(content),
                                         content_type='application/json',
                                         status=content['status'],
                                         )

        return self.HttpResponse
