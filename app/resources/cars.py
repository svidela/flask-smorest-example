from flask.views import MethodView
from flask_rest_api import Blueprint, abort

from .schemas import CarSchema, QueryByNameSchema

_ = Blueprint('Cars', 'cars',
              url_prefix='cars', description='Operations on cars')


@_.route('/')
class Cars(MethodView):

    @_.arguments(QueryByNameSchema, location='query')
    @_.response(CarSchema(many=True))
    def get(self, args):
        """List cars"""
        return []

    @_.arguments(CarSchema)
    @_.response(CarSchema, code=201)
    def post(self, new_data):
        """Add a new car"""
        return {}


@_.route('/<car_id>')
class CarsById(MethodView):

    @_.response(CarSchema)
    def get(self, car_id):
        """Get car by ID"""
        return {}

    @_.arguments(CarSchema)
    @_.response(CarSchema)
    def put(self, update_data, car_id):
        """Update existing car"""
        return {}

    @_.response(code=204)
    def delete(self, car_id):
        """Delete car"""
        abort(404, message='Item not found.')
