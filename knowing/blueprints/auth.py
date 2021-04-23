from apiflask import APIFlask, Schema, input, output, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf

from apiflask import APIBlueprint

from knowing.models import User
auth_bp = APIBlueprint('auth', __name__)

# class UserInSchema(Schema):
#     name = String(required=True, validate=Length(0, 10))
#     category = String(required=True, validate=OneOf(['dog', 'cat']))

class UserOutSchema(Schema):
    id = Integer()
    name = String()
    username = String()
    email = String()


@auth_bp.get('/users/<int:user_id>')
@output(UserOutSchema)
def get_user(user_id):
    user = User.query.get(user_id)
    return user