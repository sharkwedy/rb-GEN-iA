from marshmallow import Schema, fields, validate, ValidationError


class PersonSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    age = fields.Integer(required=True, validate=validate.Range(min=0))
    email = fields.Email(required=True)


# Example usage

def validate_person(data):
    schema = PersonSchema()
    try:
        result = schema.load(data)
        print('Valid data:', result)
    except ValidationError as err:
        print('Error:', err.messages)


# Test data
person_data = {
    'name': 'John Doe',
    'age': 30,
    'email': 'john.doe@example.com'
}
validate_person(person_data)