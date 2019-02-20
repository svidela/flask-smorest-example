from . import schemas

def register_blueprints(api):
    from . import pets, people, cars

    resources = (pets, people, cars)

    for resource_blp in (res._ for res in resources):
        # Here we can register common handlers to all resources
        #
        # resource_blp.before_request(before_request_handler)
        # resource_blp.after_request(after_request_handler)

        api.register_blueprint(resource_blp, url_prefix=f'/api/{resource_blp.url_prefix}')
