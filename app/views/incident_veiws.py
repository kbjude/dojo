import datetime
from flask.views import MethodView
from flask import request, jsonify
from app.views.validations import Validations
from app.models.incident_model import Incident


class CreateIncident(MethodView):
    def post(self):
        contentType = request.content_type
        data = request.get_json()

        # validate posted data for create incident
        validate_create_incident = Validations()
        if validate_create_incident.create_incident_validate(contentType, data) is not True:
            return validate_create_incident.create_incident_validate(contentType, data)

        # create an object from our class Incident # incident = Incident()
        incident = Incident(incident_type=data["incident_type"], title=data["title"], created_by=data["created_by"],
                            location=data["location"], status=data["status"], comment=data["comment"])

        # persist our created incident data in the database
        # we are return the most recent id in the incident list
        incident.save()
        return jsonify({
            "id": Incident.check_created_incident(data["created_by"]),
            "status": 201,
            "message": "Incident created Successfully"
        }), 201

    def get(self, incident_id):
        if incident_id is None:
            return jsonify({
                "status": 200,
                "data": Incident.get_all_incident()
            })

        return jsonify({
            "status": 200,
            "data": Incident.get_an_incident(incident_id)[0]
        }),200

    def put(self, incident_id):
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

        Incident.update_location(int(incident_id), location)
        return jsonify({
            "status": 200,
            "data": [{"id": int(incident_id),
                      "message": "Updated intervention record’s location"
                      }]
        }), 200


class Updates(MethodView):
    def put(self, incident_id):
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

        Incident.update_comment(incident_id, comment)
        return jsonify({
            "status": 200,
            "data": [{"id": int(incident_id),
                      "message": "Updated intervention record’s comment"
                      }]
        }), 200


class Status(MethodView):
    def put(self, incident_id):
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

        Incident.update_the_status(incident_id, status)
        return jsonify({
            "status": 200,
            "data": [{ "id":int(incident_id),
                      "message": "Updated  intervention record’s status"
                      }]
        })
