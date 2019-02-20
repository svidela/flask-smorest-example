from marshmallow import Schema, fields
from app import api

class QueryByNameSchema(Schema):
    name = fields.String()

    class Meta:
        strict = True


@api.definition('People')
class PersonSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String()

    pets = fields.Nested('PetSchema', many=True)
    cars = fields.Nested('CarSchema', many=True)

    class Meta:
        strict = True


@api.definition('Pet')
class PetSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String()

    owner = fields.Nested(PersonSchema)

    class Meta:
        strict = True

@api.definition('Car')
class CarSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String()

    owner = fields.Nested(PersonSchema, only=('id',))

    class Meta:
        strict = True
