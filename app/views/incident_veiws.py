import datetime
from flask.views import MethodView
from flask import request, jsonify
from app.views.validations import Validations
from app.models.incident_model import Incident
from app.views.helper import token_required


class CreateIncident(MethodView):
    @token_required
    def post(current_user, self):
   
        contentType = request.content_type
        data = request.get_json()

        # validate posted data for create incident
        validate_create_incident = Validations()
        if validate_create_incident.create_incident_validate(contentType, data) is not True:
            return validate_create_incident.create_incident_validate(contentType, data)

        # get_user_type is a method that gets us the user_id which is actually the same as our current_user.this helps us to check for is_admin is true or not if an admin then you cannotcreate incidents
        if Incident.get_user_type(current_user) == "True":
            return jsonify({
                "status":401,
                "messsage":"You donot have acess to this endpoint"
            }), 401
        # create an object from our class Incident # incident = Incident()
        # we assign current_user to be equal to created_by bcz its our foreign key and its refernced by the user id in the database 
        incident = Incident(incident_type=data["incident_type"], title=data["title"], created_by=current_user, location=data["location"], status=data["status"], comment=data["comment"])

        # persist our created incident data in the database
        # we are return the most recent id in the incident list
        incident.save()
        return jsonify({
            "incident_id": Incident.check_created_incident(current_user),
            "status": 201,
            "message": "Incident created Successfully"
        }), 201
    # this method gets all incidents and also gets us one incident
    @token_required
    def get(current_user, self, incident_id):
        if incident_id is None:
            if Incident.get_user_type(current_user) == "True":
                return jsonify({
                    "status": 200,
                    "data": Incident.get_all_incident()
                }), 200
            return jsonify({
                "status": 400,
                "message": "You cannot acess this endpoint"
            }),400

        if Incident.get_user_type(current_user):
            return jsonify({
                "status": 200,
                "data": Incident.get_an_incident(incident_id)[0]
            }),200
        
    @token_required
    def put(current_user, self, incident_id):
        location = request.json['location']
        if not isinstance(location, str):
            return jsonify({
                "Message": "Location should be a string"
            })
        if not location:
            return jsonify({
                "Message": "Location field is missing"
            })
        if location == "":
            return jsonify({
                "Message": "Location field is Empty"
            })
        try:
            int(incident_id)
        except ValueError:
            return jsonify({
                "status": 400,
                "error": "Please provide a valid Incident Id"
            }), 400

        if Incident.get_user_type(current_user) == "True":
            return jsonify({
                "status": 400,
                "message": "You donot have acess to this endpoint"
            })

        Incident.update_location(current_user, int(incident_id), location)
        return jsonify({
            "status": 200,
            "data": [{"id": int(incident_id),
                      "message": "Updated intervention record’s location"
                      }]
        }), 200


class Updates(MethodView):
    @token_required
    def put(current_user, self, incident_id):
        comment = request.json["comment"]
        if not isinstance(comment, str):
            return jsonify({
                "status": 400,
                "message": "Comment should be a string"
            }), 400

        if not comment:
            return jsonify({
                "Message": "Comment field is missing"
            })
        if comment == "":
            return jsonify({
                "Message": "Comment field is Empty"
            })
        try:
            int(incident_id)
        except ValueError:
            return jsonify({
                "status": 400,
                "error": "Please provide a valid Incident Id"
            }), 400

        if Incident.get_user_type(current_user) == "True":
            return jsonify({
                "status":400,
                "message":"You dont  have acess to this endpoint"
            }), 400

        Incident.update_comment(current_user, int(incident_id), comment)
        return jsonify({
            "status": 200,
            "data": [{"id": int(incident_id),
                      "message": "Updated intervention record’s comment"
                      }]
        }), 200


class Status(MethodView):
    @token_required
    def put(current_user, self, incident_id):
        status = request.json["status"]
        if not isinstance(status, str):
            return jsonify({
                "status": 400,
                "message": "Status must be a string"
            }), 400

        if not status:
            return jsonify({
                "status": 400,
                "message": "Status field is missing"
            }), 400

        if status == "":
            return jsonify({
                "status": 400,
                "message": "Status must not be empty"
            })

        try:
            int(incident_id)
        except ValueError:
            return jsonify({
                "status": 400,
                "error": "Please provide a valid Incident Id"
            }), 400

        if Incident.get_user_type(current_user) == "True":
            return jsonify({
                "status": 200,
                "data":Incident.update_the_status(current_user, incident_id, status),
                "message": "Updated  intervention record’s status"
            })
        return jsonify({
            "status":400,
            "message":"You dont have acces to this endpoint"
        }), 400

        
    @token_required
    def delete(current_user, self, incident_id):
        if  not isinstance(incident_id, int):
            return  jsonify({
                "status": 400,
                "message": "incident id should be a integer"
            }), 400

        # if  username and email in Incident.checkuser_exits():
        #     return jsonify({
        #         "status": 400,
        #         "message":"user already exists"
        # }) ,400

        incident_in = Incident.check_if_user_id_matches_the_incident_id(current_user, incident_id)
        print(incident_in)
        if not incident_in:
            return jsonify ({  
            "status":404, 
            "error" : "No incident record found with this id"
            }), 404

        #we can not delete a record with statuses of 'under investigation','rejected','resolved'
        #get the status which is in position 6 of the returned list

        required_status_list = ["under investigation","rejected","resolved"]
        if incident_in[0] in required_status_list:
            return jsonify({
                "status":400,
                "message":"You cannot edit, delete this status because it was updated already"
            }), 400

        Incident.delete_incident(current_user, incident_id)
        return jsonify({
            "status":200,
            "message": "Incident record deleted"
            }), 200
        return jsonify({
                "status":400,
                "message":"Sorry you donot have  to delete this Incident record"
            }), 400
