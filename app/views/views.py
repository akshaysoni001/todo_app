from flask_restful import Resource
from app import db
from flask import jsonify, make_response
import requests


class TodoApp(Resource):
    def get(self):
        projects = db.session.query(TodoApp).all()
        payload = {
            'title': projects.title,
            'person': projects.person,
            'due': projects.due,
            'status': projects.status
        }
        return make_response(jsonify(payload))

    def post(self):
        data = requests.form
        project = TodoApp(data['title'],data['person'],data['due'],data['status'])
        db.session.add(project)
        db.session.commit()

        return make_response('Project added successfully. ')