import datetime
import jwt
from app import app ,bcrypt
from flask import jsonify
from app import DatabaseConnection
cursor = DatabaseConnection.cursor()

#  create a table for users
class User:
  cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (user_id SERIAL PRIMARY KEY   NOT NULL,
                username VARCHAR(50) NOT NULL,
                password VARCHAR(50) NOT NULL,
                email VARCHAR(50) NOT NULL,
                phone_number VARCHAR(50) NOT NULL,
                is_admin VARCHAR(50) NOT NULL);''')

  def __init__(self, **kwargs):
    self.username = kwargs["username"]
    # self.password = bcrypt.generate_password_hash(kwargs["password"], app.config.get("BCRYPT_LOG_ROUNDS")).decode('utf-8')
    self.password = kwargs["password"]
    self.email = kwargs["email"]
    self.phone_number = kwargs["phone_number"]
    self.is_admin = kwargs["is_admin"]

  # Save is the same as creating user in the data base
  def save(self):
    cursor = DatabaseConnection.cursor()
    query = """
              INSERT INTO users(username, password, email, phone_number,is_admin)
              VALUES('{}', '{}', '{}', '{}', '{}')""".format(self.username, self.password,
              self.email, self.phone_number, self.is_admin)
    cursor.execute(query)
    DatabaseConnection.commit()

  # do a query to check if our user exists in the database by using the username and the email
  @staticmethod
  def check_user(username, email):
    cursor = DatabaseConnection.cursor()
    query = "SELECT row_to_json(users) FROM users WHERE username = '{}' OR email = '{}';".format(
        username, email)
    cursor.execute(query)
    user = cursor.fetchone()
    return user

  # do a query to login the user into the system
  @staticmethod
  def login_user(username):
    cursor = DatabaseConnection.cursor()
    query = "SELECT row_to_json(users) FROM users WHERE username = '{}';".format(
        username)
    cursor.execute(query)
    user_login = cursor.fetchone()
    return user_login
    if user_login and bcrypt.check_password_hash(user_login[0]['password']):
      return jsonify({
        'status': 200,
        'data': [{"token": User.encode_auth_token(user_login[0]['user_id']).decode('utf-8'), "user": user_login[0] }]
      }), 200
    return jsonify({"status":401, "error":"User does not exist or password is incorrect"}), 401

  #  do a method that is going to encode our token so that its generated
  # the token will cotains the data we want to encrpyt, expiring time
  # sub refers to the data to be encrypted
  # secret key is the key we use t encrypt the data 
        
  @staticmethod
  def encode_auth_token(user_id):
    """generate the token"""
    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "sub": user_id
        }
        # Encode our secret key and the payload
        return jwt.encode(
            payload,
            app.config["SECRET_KEY"],
            algorithm='HS256'
        )
    except Exception as error:
        return error

  @staticmethod
  # """Decoding the token to get the payload and then return the user Id in 'sub'
  #       :param token: Auth Token
  #       :return:
  #       """
  def decode_auth_token(token):
    try:
       #to decode the token, u need to pass in the token to be decoded, the key u used to encrypt it, and the method to use to decode it
      payload = jwt.decode(token, app.config["SECERT_KEY"], algorithm='HS256')
      # All our expired or invaild tokens will be stored in blacklist_token table so that they are not used again.To do this we use a class and a method to actually check if the token is valid or not
      is_token_blacklisted = BlacklistToken.check_blacklist(token)
      # check if the token provided is blacklisted or its valid
      if is_token_blacklisted:
        return "Token was blacklisted, Please login "
      return payload["sub"]

    except jwt.ExpiredSignatureError:
      return "Signature expired, Please sign in again"

    except jwt.InvalidTokenError:
      return "Invalid Key.Please sign in again"

class BlacklistToken:
  """Table to store blacklisted/invalid auth tokens"""
  cursor = DatabaseConnection.cursor()
  cursor.execute("""CREATE TABLE IF NOT EXISTS blacklist_token
  (id SERIAL PRIMARY KEY NOT NULL,
  token VARCHAR(50) NOT NULL,
  Blacklisted_on TIMESTAMP NOT NULL);""")

  def __init__(self, token):
    self.token = token
    self.Blacklisted_on = datetime.datetime.now()

  def blacklist(self):
    """Persist Blacklisted token in the database
    :return:
    """
    cursor = DatabaseConnection.cursor()
    query = "INSERT INTO blacklist_token(token, blacklisted_on) VALUES('{}', '{}')".format(self.token, self.Blacklisted_on)
    cursor.execute(query, (self.token, self.Blacklisted_on))
    cursor.commit()

  @staticmethod
  def check_blacklist(token):
    """check to find out whether a token has already been blacklisted.
    :param token: Authorization token
    :return:
    """
    cursor = DatabaseConnection.cursor()
    query = """SELECT token FROM blacklist_token WHERE token = '{}'"""
    cursor.execute(query, (token))
    response = cursor.fetchone()

    if response:
      return True
    return False
