from marshmallow import fields, validate, validates, ValidationError
from models.user import User
from app_setup import ma

class UserSchema(ma.SQLAlchemySchema):
    class Meta():
        model = User
        load_instance = True

    username = fields.String(required=True, validate=validate.Length(min=3, max=20))
    password_hash = fields.String(validate=validate.Length(min=12, max=50))
    interests = fields.List(required=True, validate=validate.Length(min=1, max=5))
    bio = fields.String(required=True, validate=validate.Length(min=5, max=100))
