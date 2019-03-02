from app.views.incident_veiws import CreateIncident, Updates, Status
from app import app


app.add_url_rule("/api/v1/incident", view_func=CreateIncident.as_view("create"), methods=["POST"])
app.add_url_rule("/api/v1/incident/<int:incident_id>", view_func=CreateIncident.as_view("get_incident"), methods=["GET"])
app.add_url_rule("/api/v1/incident", view_func=CreateIncident.as_view("get_incidents"), defaults={"incident_id": None}, methods=["GET"])
app.add_url_rule("/api/v1/incident/<int:incident_id>/location", view_func=CreateIncident.as_view("update_location"), methods=["PUT"])
app.add_url_rule("/api/v1/incident/<int:incident_id>/comment", view_func=Updates.as_view("update_comment"), methods=["PUT"])
app.add_url_rule("/api/v1/incident/<int:incident_id>/status", view_func=Status.as_view("update_status"), methods=["PUT"])
app.add_url_rule("/api/v1/incident/<int:incident_id>", view_func=Status.as_view("delete_incident"), methods=["DELETE"])