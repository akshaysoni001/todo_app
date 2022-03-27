class Development:
    MYSQL_HOST = ''
    MYSQL_USER_NAME = ''
    MYSQL_PASSWORD = ''
    MYSQL_DATABASE_NAME = "todo_db"  # db database name
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{MYSQL_USER_NAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE_NAME}'


config = Development
