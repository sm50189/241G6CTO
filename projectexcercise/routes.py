def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('frontPage', '/')
    config.add_route('feedpage','/home/{page_number}')
    config.add_route('pageView','/view_project/{id_project}')
