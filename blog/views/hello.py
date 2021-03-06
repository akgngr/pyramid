from pyramid.view import view_config
from pyramid.response import Response

@view_config(
    route_name='hello',
    renderer='../templates/hello.jinja2'
)
def home(request):
    return { 'mesaj':'Hello World!' }

@view_config(
    route_name='test-hello',
    renderer='json'
)
def testhello(request):
    return{'content': 'Hello!'}