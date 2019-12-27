def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('merhaba', '/merhaba')
    config.add_route('api', '/api')
    config.add_route('hello', '/helloworld')
    config.add_route('test-hello','/test-hello')