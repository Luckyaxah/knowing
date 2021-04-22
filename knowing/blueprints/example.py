from apiflask import APIFlask, Schema, input, output, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf

from apiflask import APIBlueprint
example_bp = APIBlueprint('example',__name__)
pets = [
    {
        'id': 0,
        'name': 'Kitty',
        'category': 'cat'
    },
    {
        'id': 1,
        'name': 'Coco',
        'category': 'dog'
    }
]


class PetInSchema(Schema):
    name = String(required=True, validate=Length(0, 10))
    category = String(required=True, validate=OneOf(['dog', 'cat']))


class PetOutSchema(Schema):
    id = Integer()
    name = String()
    category = String()


@example_bp.get('/')
def say_hello():
    # returning a dict equals to use jsonify()
    return {'message': 'Hello!'}


@example_bp.get('/pets/<int:pet_id>')
@output(PetOutSchema)
def get_pet(pet_id):
    if pet_id > len(pets) - 1:
        abort(404)
    # you can also return an ORM model class instance directly
    return pets[pet_id]


@example_bp.put('/pets/<int:pet_id>')
@input(PetInSchema)
@output(PetOutSchema)
def update_pet(pet_id, data):
    # the parsed input data (dict) will be injected into the view function
    if pet_id > len(pets) - 1:
        abort(404)
    data['id'] = pet_id
    pets[pet_id] = data
    return pets[pet_id]

@example_bp.post('/pets')
@input(PetInSchema)
@output(PetOutSchema)
def create_pet(data):
    pet = Pet(**data)
    print(data)
    return pet

@example_bp.patch('/pets/<int:pet_id>')
@input(PetInSchema)
@output(PetOutSchema)
def update_pet(pet_id, data):
    pet = Pet.query.get(pet_id)
    for attr, value in data.items():
        setattr(pet, attr, value)
    return pet