from flask.views import MethodView
from flask_smorest import Blueprint, abort

from .schemas import PetSchema, QueryByNameSchema

_ = Blueprint('Pets', 'pets',
              url_prefix='pets', description='Operations on pets')


@_.route('/')
class Pets(MethodView):

    @_.arguments(QueryByNameSchema, location='query')
    @_.response(200, PetSchema(many=True))
    def get(self, args):
        """List pets"""
        return []

    @_.arguments(PetSchema)
    @_.response(201, PetSchema)
    def post(self, new_data):
        """Add a new pet"""
        return {}


@_.route('/<pet_id>')
class PetsById(MethodView):

    @_.response(200, PetSchema)
    def get(self, pet_id):
        """Get pet by ID"""
        return {}

    @_.arguments(PetSchema)
    @_.response(200, PetSchema)
    def put(self, update_data, pet_id):
        """Update existing pet"""
        return {}

    @_.response(204)
    def delete(self, pet_id):
        """Delete pet"""
        abort(404, message='Item not found.')
