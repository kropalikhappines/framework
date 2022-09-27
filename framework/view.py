from main.templator import render
from patterns.creation_patterns import Main, Logger
from patterns.structure_patterns import AppUrl

patt = Main()
logger = Logger('main')
routes = {}


# routes = {
#     '/': Index(),
#     '/examples/': ExampleView(),
#     '/page/': PageView(),
#     '/anotherpage/': AnotherView(),
#     '/contact/': ContactView(),
#     '/category/': CategoryView(),
#     '/create_category/': CreateCategoryView(),
#     '/category_course/': CourseView(),
#     '/create_course/': CreateCourseView(),
#     '/create_copy_course/': CopyCourse(),
#
# }
@AppUrl(routes=routes, url='/')
class Index:
    def __call__(self, request):
        return '200 OK', render('index.html')


@AppUrl(routes=routes, url='/examples/')
class ExampleView:
    def __call__(self, request):
        return '200 OK', render('examples.html')


@AppUrl(routes=routes, url='/page/')
class PageView:
    def __call__(self, request):
        return '200 OK', render('page.html')


@AppUrl(routes=routes, url='/anotherpage/')
class AnotherView:
    def __call__(self, request):
        return '200 OK', render('another_page.html')


@AppUrl(routes=routes, url='/contact/')
class ContactView:
    def __call__(self, request):
        return '200 OK', render('contact.html')


@AppUrl(routes=routes, url='/category/')
class CategoryView:
    def __call__(self, request):
        logger.log('Список категорий')
        categories = patt.categories
        return '200 OK', render('category.html', object_list=categories)


@AppUrl(routes=routes, url='/create_category/')
class CreateCategoryView:
    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            name = data['your_name']
            name = patt.decode_value(name)

            s = patt.create_category(name)
            patt.categories.append(s)
            return '200 OK', render('category.html', object_list=patt.categories)
        else:
            categories = patt.categories

            return '200 OK', render('create_category.html', object_list=categories)


@AppUrl(routes=routes, url='/category_course/')
class CourseView:
    def __call__(self, request):
        logger.log('Список кусов')
        print(request)
        category = patt.find_category_id(int(request['data']['id']))
        return '200 OK', render('course.html', object_list=category.courses,
                                id=category.id)


@AppUrl(routes=routes, url='/create_course/')
class CreateCourseView:

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            name = data['your_name']
            name = patt.decode_value(name)
            category = patt.find_category_id(self.category_id)
            s = patt.create_course('record', name, category)
            patt.courses.append(s)
            for i in category.courses:
                print(i,'for in')
            # print(category.courses.id)
            return '200 OK', render('course.html', object_list=category.courses,
                                    name=category.name,
                                    id=self.category_id)
        else:
            self.category_id = [int(s) for s in request['data']['id'] if s.isdigit()][0]
            category = patt.find_category_id(self.category_id)
            return '200 OK', render('create_course.html', object_list=category.name,
                                    id=category.id)


@AppUrl(routes=routes, url='/create_copy_course/')
class CopyCourse:
    def __call__(self, request):

        get_id = request['data']['id']
        course = patt.get_item_course(get_id)
        category_id = course.category.id
        new_name = f'copy_{course.name}'
        category = patt.find_category_id(category_id)
        s = patt.create_course('record', new_name, category)
        patt.courses.append(s)
        return '200 OK', render('course.html', object_list=category.courses,
                                name=category.name,
                                id=category_id)
