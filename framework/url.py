from view import index_view, example_view, page_view, another_view, contact_view


routes = {
    '/': index_view,
    '/examples/': example_view,
    '/page/': page_view,
    '/anotherpage/': another_view,
    '/contact/': contact_view,
}