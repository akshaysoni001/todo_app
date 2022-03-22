from app import db
from datetime import datetime


class TodoApp(db.Model):
    __tablename__="todo_projects"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    person = db.Column(db.String(255))
    due = db.Column(db.DateTime)
    status = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, title, person, due, status):
        self.title = title
        self.person = person
        self.due = due
        self.status = status

