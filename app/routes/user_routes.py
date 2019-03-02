from app.views.user_veiws import SignupUser, LoginUser
from app import app


app.add_url_rule("/api/v1/auth/signup", view_func= SignupUser.as_view("signup"), methods=["POST"])
app.add_url_rule("/api/v1/auth/login", view_func= LoginUser.as_view("login"), methods=["POST"])
