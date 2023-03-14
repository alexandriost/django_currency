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

        total_time_ms = int(total_time * 1000)

        # print(f'Total time: {total_time_ms} ms')

        # RequestResponseLog.objects.create(path=..., method=..., time=...)

        RequestResponseLog.objects.create(path=request.path, request=request.method, time=total_time_ms)

        return response
