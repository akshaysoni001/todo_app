from app.models.models import TodoApp
from app import db
from datetime import datetime


def seed_projects():
    db.session.add(TodoApp(title='Native Vista', person='Akshay Soni', status='ongoing'))
    db.session.commit()

seed_projects()