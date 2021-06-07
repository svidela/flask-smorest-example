from flask import current_app
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from .schemas import CarSchema, QueryByNameSchema

_ = Blueprint('Cars', 'cars',
              url_prefix='cars', description='Operations on cars')


@_.route('/')
class Cars(MethodView):

    @_.arguments(QueryByNameSchema, location='query')
    @_.response(200, CarSchema(many=True))
    def get(self, args):
        """List cars"""
        return []

    @_.arguments(CarSchema)
    @_.response(201, CarSchema)
    def post(self, new_data):
        """Add a new car"""
        return {}


@_.route('/<car_id>')
class CarsById(MethodView):

    @_.response(200, CarSchema)
    def get(self, car_id):
        """Get car by ID"""
        return {
            'id': 1, 
            'name': current_app.config['SOME_CONFIG'],
            'owner': {
                'id': 1,
                'name': 'Foo Bar'
            }
        }

    @_.arguments(CarSchema)
    @_.response(200, CarSchema)
    def put(self, update_data, car_id):
        """Update existing car"""
        return {}

    @_.response(204)
    def delete(self, car_id):
        """Delete car"""
        abort(404, message='Item not found.')
