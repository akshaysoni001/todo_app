from app import api
from app.views.views import TodoApp

api.add_resource(TodoApp, '/todoapp')
