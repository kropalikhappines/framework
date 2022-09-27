s = dict(categories=[{
    'id': 1,
    'name': 'one_cat',
    'course': [
        'one_course', 'two_course'
    ]
},
    {
        'id': 2,
        'name': 'two_cat',
        'course': [
            'one_course', 'two_course'
        ]
    }])

for i in s['categories']:
    print(i)
