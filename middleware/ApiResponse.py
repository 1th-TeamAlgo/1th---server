import re
from rest_framework.status import is_client_error


class ResponseFormattingMiddleware:
    METHOD = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')

    def __init__(self, get_response):
        self.get_response = get_response
        self.API_URLS = [
            re.compile(r'^(.*)/api/v1'),
            re.compile(r'^api/v1'),
        ]

    def __call__(self, request):
        response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

    def process_response(self, request, response):
        print(request.path_info)
        path = request.path_info
        valid_urls = (url.match(path) for url in self.API_URLS)

        if request.method in self.METHOD and any(valid_urls):
            response_format = {
                'code': "200",
                'status': "OK",
                'message': {}

            }

            if hasattr(response, 'data') and getattr(response, 'data') is not None:
                data = response.data
                try:
                    response_format['message'] = data.pop('message')
                except (KeyError, TypeError):
                    response_format.update({
                        'code': response.status_code,
                        'status': response.status_text,
                        'message': data,

                    })

                    response.data = response_format
                    response.content = response.render().rendered_content
            else:
                response.data = response_format

        return response
