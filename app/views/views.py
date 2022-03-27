from flask_restful import Resource
from app import db
from flask import jsonify, make_response, request
import requests
from app.models.models import TodoApp


class TodoAppView(Resource):

    def get(self):
        projects = db.session.query(TodoApp).all()
        payload = []
        if projects:
            for project in projects:
                data = {
                    'title': project.title,
                    'person': project.person,
                    'due': project.due,
                    'status': project.status,
                    'content': project.content
                }
                payload.append(data)

            return make_response(jsonify(payload))

    def post(self):
        try:
            data = request.json
            project = TodoApp(title=data['title'], person=data['person'], status=data['status'],
                              due=data['due'], content=data['content'])
            db.session.add(project)
            db.session.commit()
            return make_response('Project added successfully. ')
        except Exception as e:
            return make_response(e)
