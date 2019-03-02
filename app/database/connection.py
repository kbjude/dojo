from app import app
import psycopg2
import psycopg2.extras


try:

    DatabaseConnection = psycopg2.connect(
        database=app.config["DATABASE_NAME"],
        password=app.config["DATABASE_PASSWORD"],
        user=app.config["DATABASE_USER"],
        host=app.config["DATABASE_HOST"],
        port=5432
    )

    DatabaseConnection.autocommit = True

    dict_cursor = DatabaseConnection.cursor(
        cursor_factory=psycopg2.extras.RealDictCursor)
    cursor = DatabaseConnection.cursor()

    app.logger.info('Database connection successful')

except Exception as e:
    app.logger.error('Database Error: %s', str(e))
