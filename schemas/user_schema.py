from extensions import ma
from models.user import User
from marshmallow import fields, validate

class UserSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = User  # links the schema to User model 
    load_instance= True # makes schema.load() return a real User object instead of a dict.

  email = fields.Email(required=True)
  password = fields.String(required=True, validate=validate.Length(min=8),load_only=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

