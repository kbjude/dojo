from app.views.incident_veiws import CreateIncident
from app.views.incident_veiws import Updates
from app.views.incident_veiws import Status

class IncidentUrl:
  @staticmethod
  def get_incident_routes(app):
    create_incident_veiw = CreateIncident.as_view("create_an_incident")
    app.add_url_rule("/incident", view_func=create_incident_veiw, methods=["POST"])
    app.add_url_rule("/incident/<int:incident_id>", view_func=create_incident_veiw, methods=["GET"])
    app.add_url_rule("/incident", view_func=create_incident_veiw, defaults={"incident_id": None}, methods=["GET"])
    app.add_url_rule("/incident/<int:incident_id>/location", view_func=create_incident_veiw, methods=["PUT"])


class UpdateUrl:
  @staticmethod
  def update_the_comment_routes(app):
    Update_comment_veiw = Updates.as_view("update_a_comment")
    app.add_url_rule("/incident/<int:incident_id>/comment", view_func=Update_comment_veiw, methods=["PUT"])

class UpdateStatus:
  @staticmethod
  def update_status(app):
    Update_status_veiw = Status.as_view("update_a_status")
    app.add_url_rule("/incident/<int:incident_id>/status", view_func=Update_status_veiw, methods=["PUT"])
    app.add_url_rule("/incident/<int:incident_id>", view_func=Update_status_veiw, methods=["DELETE"])