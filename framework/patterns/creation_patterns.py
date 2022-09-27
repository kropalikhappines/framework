from quopri import decodestring


class Category:
    id_category = 0

    def __init__(self, name):
        self.id = Category.id_category
        Category.id_category += 1
        self.name = name
        self.courses = []


class Course:
    id_course = 0

    def __init__(self, name, category):
        self.id = Course.id_course
        Course.id_course += 1
        self.name = name
        self.category = category
        self.category.courses.append(self)


class RecordCourse(Course):
    pass


class InteractiveCourse(Course):
    pass


class CoursesKinds:
    kinds = {
        'record': RecordCourse,
        'interactive': InteractiveCourse
    }

    @classmethod
    def create(cls, kind, name, category):
        return cls.kinds[kind](name, category)


class Main:
    def __init__(self):
        self.categories = []
        self.courses = []

    @staticmethod
    def create_category(name):
        return Category(name)

    @staticmethod
    def create_course(kind, name, category):
        return CoursesKinds.create(kind, name, category)

    def find_category_id(self, id):

        for item in self.categories:
            if item.id == id:
                return item

    @staticmethod
    def decode_value(val):
        val_b = bytes(val.replace('%', '=').replace("+", " "), 'utf-8')
        val_decode_str = decodestring(val_b)

        return val_decode_str.decode('utf-8')

    def get_item_course(self, id):
        for item in self.courses:
            print(item.id, 'sadas')

            if item.id == int(id):
                print(item.id)
                return item


class SingletonByName(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        if args:
            name = args[0]
        if kwargs:
            name = kwargs['name']

        if name in cls.__instance:
            return cls.__instance[name]
        else:
            cls.__instance[name] = super().__call__(*args, **kwargs)
            return cls.__instance[name]


class Logger(metaclass=SingletonByName):

    def __init__(self, name):
        self.name = name

    @staticmethod
    def log(text):
        print('log--->', text)
