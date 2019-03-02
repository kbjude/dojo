# Ireporter
by The dojos


I-Reporter is a platform where the public can report incidents of corruption plus anything else that is affecting them to call for government internvetion.

## Users can do the following;
  - Create a ​red-flag​​ record
  - Get all ​red-flag​​ records
  - Get a specific ​red-flag​​ record
  - Edit a specific ​red-flag​​ record
  - Delete a ​red-flag​​ record


## Prerequisties:
Inorder  to run this application you need the following;
  - Install python. [python3](https://www.python.org/downloads/)
  - Install Postgres database.


## Installation:
  - Clone this repository.
  - Setup a virtual environment and activate it.
  - Install the requirements.txt
  - Add a ".env" file that has:
    - DATABASE_NAME=your_database_name
    - DATABASE_USER=your_database_username
    - DATABASE_HOST=your_database_host
    - DATABASE_PASSWORD=your_user_password
    - DATABASE_PORT=your_database_port_number
    - SECRET_KEY=your_secret_key


## Running the application:
  Open the directory of the application in the terminal and execute "flask run".
  
  In a browser type the Url: http//localhost:5000.


## Supported Endpoints
| Method | Endpoint                                 | Description                     |
| ------ | ---------------------------------------- | ------------------------------- |
| POST   | /api/v1/register/                        | Create User                     |
| POST   | /api/v1/login/                           | Log in User                     |
| POST   | /api/v1/incident/                        | Create red flag or intervention |
| GET    | /api/v1/incident/all                     | Get all created incidents       |
| GET    | /api/v1/incident/<incident_id>/          | Get specific red flag           |
| PATCH  | /api/v1/incident/<incident_id>/location/ | Edit red flag location          |
| PATCH  | /api/v1/incident/<incident_id>/comment/  | Edit red flag comment           |
| DELETE | /api/v1/red-flags/<incident_id>/         | Delete red flag                 |
