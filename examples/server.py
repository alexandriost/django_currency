def hello():
    return b'Hello'


def world():
    return b'world'


urlpatterns = {
    '/hello/': hello,
    '/world/': world
}


def app(environ, start_response):
    path = environ['RAW_URI']
    view_func = urlpatterns.get(path)

    if not view_func:
        data = b'Not Found'
        start_response("404 Not Found", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])

    data = view_func()

    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
