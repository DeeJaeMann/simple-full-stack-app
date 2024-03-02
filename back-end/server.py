#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

str_app_ep = "/api/v1/"

server = Flask(__name__)
# start a flask app with Cross Origin Resource Sharing capabilities
# set CORS resources
cors = CORS(server, resources={r"/api/*": {"origins": "*"}})

# connect flask app to PostgreSQL
server.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://deemann@localhost/cp-simple-fs'

db = SQLAlchemy(server)

# create Subject Model
class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    difficulty_level = db.Column(db.Integer)
    description = db.Column(db.String)

# create Instructor Model
class Instructors(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    description = db.Column(db.String)


# Base endpoint (home page with links to endpoints)
@server.route("/", methods=['GET'])
def display_home() :
    str_result = """
<h1>cp-simple-fs API Server Home</h1>
<ul>
"""
    str_result += f"<li><a href=\"{str_app_ep}subjects/\">Get Subjects</a></li>"
    str_result += f"<li><a href=\"{str_app_ep}instructors/\">Get Instructors</a></li>"
    str_result += "</ul>"

    return str_result

# create an endpoint for 'api/v1/subjects/' that returns all subjects sorted by difficulty level 1-4
@server.route(f"{str_app_ep}subjects/", methods=['GET'])
# @cross_origin
def get_subjects() :
    return "<h1>Subjects</h1>"
# create an endpoint for 'api/v1/instructors/' that returns all instructors sorted from oldest to youngest
@server.route(f"{str_app_ep}instructors/", methods=['GET'])
# @cross_origin
def get_instructors() :
    return "<h1>Instructors</h1>"
# run your server

if __name__ == '__main__' :
    server.run(debug=True)