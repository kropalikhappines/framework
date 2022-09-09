from wsgiref.simple_server import make_server


def index_view():
    return '200 OK', [b'Index']


def abc_view():
    return '200 OK', [b'abc']


def not_found():
    return '404 BAD', [b'404 Page not found']


class Other:
    def __call__(self, *args, **kwargs):
        return '200 OK', [b'other']


routes = {
    '/': index_view,
    '/abc/': abc_view,
    '/other/': Other()
}


class Application:
    def __init__(self, routes):
        self.routers = routes

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        print(path + '/')
        if not path.endswith('/'):
            path = path + '/'
        if path in self.routers:
            view = self.routers[path]
        else:
            view = not_found
        code, body = view()
        start_response(code, [('Content-Type', 'text/html')])
        return body


application = Application(routes)


with make_server('', 8000, application) as httpd:
    print('Serving on port 8000...')
    httpd.serve_forever()
