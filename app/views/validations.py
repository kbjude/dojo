import datetime
import re
from flask import request, jsonify
from app.models.user_model import User


class Validations:
    def create_user_validation(self, contentType, data):

        if contentType != "application/json":
            return jsonify({
                "status": 400,
                "message": " Wrong content Type"
            }), 400

        if "username" not in data or "password" not in data or "email" not in data or "phone_number" not in data or "is_admin" not in data:
            return jsonify({
                "status": 400,
                "message": "wrong Body Format"
            }), 400

        username = data.get("username")
        password = data.get("password")
        email = data.get("email")
        phone_number = data.get("phone_number")
        is_admin = data.get("is_admin")
    
        if not username or not email or not phone_number or not password:
            return jsonify({
                "status": 400,
                "message": ["username/email/phone number/is_Admin/should not be empty", "password should not be empty"]
            }), 400

        if not isinstance(username, str) or not isinstance(email, str) or not isinstance(is_admin,bool) or not isinstance(phone_number, int):
            return jsonify({
                "status": 400,
                "message": "username/email/should be strings,A phone number should be an integer, is_admin should be a Boolean"
            }), 400
            
        if  not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return jsonify({
                "status":400,
                "message": "Wrong format of the email"
            }), 400

        if re.search("[0-9]", username):
            return jsonify({
                "status":400,
                "message": "Username should not contain digits"
            }), 400
       
        # check if the user is in the database by using the email and the username
        user = User.check_user(username, email)
        if user:
            return jsonify({
                "status": 400,
                "message": "User already exists,Please check your username or email"
            }), 400
        return True

    def login_validations(self, contentType, data):
        if contentType != "application/json":
            return jsonify({
                "status": 400,
                "message": "The application content should be json"
            }), 400

        if "username" not in data and "password" not in data:
            return jsonify({
                "status": 400,
                "message": "Wrong body Fomat"
            }), 400

        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({
                "status": 400,
                "message": "Please feilds must not be empty"
            }), 400

        if not isinstance(username, str) and len(password) < 5:
            return jsonify({
                "status": 400,
                "message": "Please your username should be a string and Password must be more than 5 characters"
            }), 400
        return True

    def create_incident_validate(self, contentType, data):
        if contentType != "application/json":
            return jsonify({
                "status": 400,
                "message": "The application content type must be json"
            }), 400

        if "incident_type" not in data or "title" not in data or "location" not in data or "status" not in data or "comment" not in data:
            return jsonify({
                "status": 400,
                "message": "Wrong body format"
            }), 400
        data = request.get_json()
        incident_type = data.get("incident_type")
        title = data.get("title")
        created_on = datetime.datetime.now()
        location = data.get("location")
        status = data.get("status")
        comment = data.get("comment")

        if not isinstance(incident_type, str) and not isinstance(title, str)  and not isinstance(location, str) and not isinstance(status, str) and not isinstance(comment, str):
            return jsonify({
                "status": 400,
                "message":"Fields must be Strings"
            }), 400

        if not incident_type and not title  and not location and not status and not comment:
            return jsonify({
                "status": 400,
                "message": "Felids must not be empty"
            }), 400
        return True
