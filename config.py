class Development:
    MYSQL_HOST = "localhost"  # host
    MYSQL_USER_NAME = "sla"  # db username
    MYSQL_PASSWORD = "sla"  # db password
    MYSQL_DATABASE_NAME = "sla_db"  # db database name
    DEBUG =True
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{MYSQL_USER_NAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE_NAME}'


config = Development
