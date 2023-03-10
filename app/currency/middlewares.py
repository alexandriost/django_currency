from time import time
from currency.models import RequestResponseLog


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()

        response = self.get_response(request)

        end = time()

        total_time = end - start

        # print(f'Total time: {end - start}')

        # RequestResponseLog.objects.create(path=..., method=..., time=...)

        RequestResponseLog.objects.create(path=request.path, request=request.method, time=total_time)

        return response
