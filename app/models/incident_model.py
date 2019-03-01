import datetime
from app import DatabaseConnection

cursor = DatabaseConnection.cursor()

class Incident:
 
  def __init__(self, **kwargs):
    self.incident_type = kwargs["incident_type"]
    self.title = kwargs["title"]
    self.created_by = kwargs["created_by"]
    self.location = kwargs["location"]
    self.status = kwargs["status"]
    self.comment = kwargs["comment"]           

  #  save is the same as create incident in the database
  def save(self):
    cursor = DatabaseConnection.cursor()

    query = """
            INSERT INTO incident(incident_type, title, created_by, location, status, comment)
            VALUES('{}','{}', '{}', '{}', '{}', '{}')""".format(self.incident_type, self.title, self.created_by, self.location, self.status, self.comment)
    cursor.execute(query)
    DatabaseConnection.commit()

  @staticmethod
  def check_created_incident(created_by):
    cursor = DatabaseConnection.cursor()
    #this query returns the most recent id in the table and it requires the table name and the column name want to use
    query = """SELECT currval(pg_get_serial_sequence('{}', '{}'))""".format("incident", "incident_id")
    cursor.execute(query)
    Incidents = cursor.fetchone()
    #return the id which is in position zero of list incident
    return Incidents[0]

  @staticmethod
  def get_an_incident(incident_id):
    cursor = DatabaseConnection.cursor()
    query = "SELECT row_to_json(incident) FROM incident WHERE incident_id = '{}';".format(incident_id)
    cursor.execute(query)
    incidents = cursor.fetchone()
    return incidents

  @staticmethod
  def get_all_incident():
    DatabaseConnection.cursor()
    query = "SELECT row_to_json(incident) FROM incident"
    cursor.execute(query)
    all_incidents = cursor.fetchall()
    return all_incidents

  @staticmethod
  def update_location(user_id, incident_id, location):
    DatabaseConnection.cursor()
    query = "UPDATE incident SET location = '{}' WHERE incident_id = '{}';".format(location, incident_id)
    cursor.execute(query)
   
  @staticmethod
  def update_comment(user_id, incident_id, comment):
    DatabaseConnection.cursor()
    query = "UPDATE incident SET comment = '{}' WHERE incident_id = '{}';".format(comment, incident_id)
    cursor.execute(query)

  @staticmethod
  def update_the_status(user_id, incident_id, status):
    DatabaseConnection.cursor()
    query = "UPDATE incident SET status = '{}' WHERE incident_id = '{}';".format(status, incident_id)
    cursor.execute(query)
  
  @staticmethod
  def get_user_type(user_id):
    DatabaseConnection.cursor()
    query = "SELECT is_admin FROM users WHERE user_id = '{}'".format(user_id)
    cursor.execute(query)
    get_the_user = cursor.fetchone()
    return get_the_user[0]

  @staticmethod
  def delete_incident(user_id, incident_id):
    DatabaseConnection.cursor()
    query = "DELETE FROM incident WHERE incident_id = '{}'".format(incident_id)
    cursor.execute(query)

  @staticmethod
  def drop_tables():
    DatabaseConnection()
    queries = (
      """DROP TABLE IF EXISTS incident(
                incident_id SERIAL PRIMARY KEY,
                incident_type VARCHAR(225) NOT NULL,
                title VARCHAR(225) NOT NULL,
                created_by INTEGER NOT NULL,
                location VARCHAR(225) NOT NULL,
                status  VARCHAR(225) DEFAULT 'draft',
                comment VARCHAR(225),
                created_on TIMESTAMP DEFAULT Now(),
                FOREIGN KEY (created_by)
                  REFERENCES users (user_id)
                  ON UPDATE CASCADE ON DELETE CASCADE,
                  )
                
                """,

                """
                DROP TABLE IF EXISTS users(
                user_id SERIAL PRIMARY KEY   NOT NULL,
                username VARCHAR(225) NOT NULL,
                password VARCHAR(225) NOT NULL,
                email VARCHAR(225) NOT NULL,
                phone_number VARCHAR(225) NOT NULL,
                is_admin VARCHAR(225) NOT NULL
                )
                
                """
      )
    

    for query in queries:
      cursor.execute(query)
    cursor.close()
  

  # @staticmethod
  # def checkuser_exits():
  #   DatabaseConnection.cursor()
  #   query = "SELECT user_id from users WHERE username = '{}' AND email = '{}'".format(email, username)
  #   cursor.execute(query)
  #   user_got = cursor.fetchone()
  #   #get users id w/c is in position 0 of the returned list
  #   return user_got[0]

#check for the record matching the user's id and incident id
  @staticmethod
  def  check_if_user_id_matches_the_incident_id(created_by, incident_id):
    DatabaseConnection.cursor()
    query = "SELECT status FROM incident WHERE created_by = '{}' AND incident_id = '{}'".format(created_by, incident_id)
    cursor.execute(query)
    incident_matching = cursor.fetchone()
    return incident_matching
    