from main.templator import render


def index_view():
    return '200 OK', render('index.html')


def example_view():
    return '200 OK', render('examples.html')


def page_view():
    return '200 OK', render('page.html')


def another_view():
    return '200 OK', render('another_page.html')


def contact_view():
    return '200 OK', render('contact.html')


# class Other:
#     def __call__(self, *args, **kwargs):
#         return '200 OK', [b'other']