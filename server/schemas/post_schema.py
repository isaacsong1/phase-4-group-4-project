from . import fields, validate
from models.post import Post
from app_setup import ma


class PostSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Post
        load_instance = True

    title = fields.String(required=True, validate=validate.Length(min=2, max=30))
    content = fields.String(required=True, validate=validate.Length(min=3, max=3000))
