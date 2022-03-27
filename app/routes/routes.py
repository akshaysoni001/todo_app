from app import api
from app.views.views import TodoAppView

api.add_resource(TodoAppView, '/todoapp')
