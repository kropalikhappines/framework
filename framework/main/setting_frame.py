from quopri import decodestring
from .requests_frame import GetRequest, PostRequest


def not_found():
    return '404 BAD', '404 Page not found'


class Application:
    def __init__(self, routes):
        self.routers = routes

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path = f'{path}/'
        request = {}
        method = environ['REQUEST_METHOD']

        request['method'] = method
        if method == 'GET':
            result = GetRequest.get_request_pars(environ['QUERY_STRING'])
            request['data'] = Application.decoder(result)
        if method == 'POST':
            result = PostRequest().get_requests(environ)
            request['data'] = Application.decoder(result)
            print(request)
        if path in self.routers:
            view = self.routers[path]
        else:
            view = not_found

        code, body = view()
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decoder(data):
        result = {}
        for key, value in data.items():
            val = bytes(value.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = decodestring(val).decode('UTF-8')
            result[key] = val_decode_str
        return result

