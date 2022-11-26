from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projects.db" #connect to SQLAlchemy to database
db = SQLAlchemy(app) #creates the extension


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Project Title', db.String())
    completion_date = db.Column('Completion Date', db.DateTime)
    description = db.Column('Description', db.Text())
    skills = db.Column('Skills', db.Text())
    github = db.Column('GitHub Link', db.String())


    def __repr__(self):
        return f'''Project Title: {self.title}
                Completion Date: {self.completion_date}
                Description: {self.description}
                Skills: {self.skills}
                GitHub Link: {self.github}'''
