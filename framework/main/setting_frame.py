def not_found():
    return '404 BAD', '404 Page not found'


class Application:
    def __init__(self, routes):
        self.routers = routes

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path = f'{path}/'
        if path in self.routers:
            view = self.routers[path]
        else:
            view = not_found

        code, body = view()
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

