from flask.views import MethodView
from flask_rest_api import Blueprint, abort

from .schemas import PersonSchema, QueryByNameSchema

_ = Blueprint('People', 'people',
              url_prefix='people', description='Operations on people')


@_.route('/')
class People(MethodView):

    @_.arguments(QueryByNameSchema, location='query')
    @_.response(PersonSchema(many=True))
    def get(self, args):
        """List people"""
        return []

    @_.arguments(PersonSchema)
    @_.response(PersonSchema, code=201)
    def post(self, new_data):
        """Add a new person"""
        return {}


@_.route('/<person_id>')
class PeopleById(MethodView):

    @_.response(PersonSchema)
    def get(self, person_id):
        """Get person by ID"""
        return {}

    @_.arguments(PersonSchema)
    @_.response(PersonSchema)
    def put(self, update_data, person_id):
        """Update existing person"""
        return {}

    @_.response(code=204)
    def delete(self, person_id):
        """Delete person"""
        abort(404, message='Item not found.')
