from app import DatabaseConnection
from flask.views import MethodView
from flask import request ,jsonify
from app.views.validations import Validations
from app.models.user_model import User
from app.views.helper import token_required
from flask_bcrypt import Bcrypt



class SignupUser(MethodView):
  def post(self):
    data = request.get_json()
    contentType = request.content_type
 
    #validate posted data for create user
    validate = Validations()
    if validate.create_user_validation(contentType, data) is not True:
      return validate.create_user_validation(contentType, data)

    # we ceate an object user from our class User
    user = User(username=data["username"], password=data["password"], email=data["email"], phone_number=data["phone_number"], is_admin=data["is_admin"])
    
    # persist user in the database 
    user.save()
    return jsonify({
      "status":201,
      "message": "User created successfully",
      "data":User.check_user(data["username"], data["email"])[0]
    }), 201


class LoginUser(MethodView):
  def post(self):
    data = request.get_json()
    contentType = request.content_type

    validate_login = Validations()
    if validate_login.login_validations(contentType, data) is not True:
      return validate_login.login_validations(contentType, data)

    login = User.login_user(data["username"])
    if login:
      return jsonify({
        "status":200,
        "message":"Login successful"
      }), 200
