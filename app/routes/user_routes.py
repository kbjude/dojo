from app.views.user_veiws import SignupUser
from app.views.user_veiws import LoginUser

class UserUrl:
  @staticmethod
  def get_user_routes(app):
    register_user_view = SignupUser.as_view("create_user") 
    log_user_view = LoginUser.as_view("login_a_user")
    app.add_url_rule("/auth/signup", view_func= register_user_view, methods=["POST"])
    app.add_url_rule("/auth/login", view_func= log_user_view, methods=["POST"])
