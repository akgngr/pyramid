from pyramid.view import view_config
from pyramid.response import Response
from pyramid.events import NewRequest
from pyramid.events import NewResponse
from pyramid.events import subscriber

liste = ['ahmet', 'mehmet', 'ayşe', 'leyla']

@view_config(route_name='merhaba', renderer='../templates/merhaba.jinja2')
def hello(request):
    return {'project': 'Merhaba pyramid projeme hoşgeldiniz', 'liste': liste}

@view_config(
    route_name="api",
    renderer="json"
)
def api(request):
    return {'a':1,'b':2}

@subscriber(NewRequest, NewResponse)
def mysubscriber(event):
    print(event)