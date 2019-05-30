from marshmallow import Schema, fields


class QueryByNameSchema(Schema):
    name = fields.String()

    class Meta:
        strict = True


class PersonSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String()

    pets = fields.Nested('PetSchema', many=True)
    cars = fields.Nested('CarSchema', many=True)

    class Meta:
        strict = True


class PersonNestedSchema(PersonSchema):
    class Meta:
        fields = ('id', 'name')


class PetSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String()

    owner = fields.Nested(PersonSchema)

    class Meta:
        strict = True


class CarSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String()

    owner = fields.Nested(PersonNestedSchema)

    class Meta:
        strict = True
