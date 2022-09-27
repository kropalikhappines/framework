from wsgiref.simple_server import make_server
from main.setting_frame import Application
from view import routes


application = Application(routes)


def runserver():
    with make_server('', 8000, application) as httpd:
        print('Serving on port 8000...')
        httpd.serve_forever()


if __name__ == '__main__':
    runserver()
