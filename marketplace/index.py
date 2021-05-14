# This is the index of the app, where all the routes are defined. Defined routes are GET /projects to get all projects.
# GET /projects/id to get a project by with it information, if it has no offers it min_amount will figure as null.
# POST /projects to create new projects and POST /offer to post new offers to a project by ID.


from flask import Flask, jsonify, request
import json
import sys
from marketplace.model.project import Project, ProjectSchema
from marketplace.model.offer import Offer, OfferSchema

app = Flask(__name__)

all_projects = []


@app.route("/projects/<string:pk>")
def get_project_by_id(pk):
    for project in all_projects:
        if str(project.id) == pk:
            schema = ProjectSchema(many=False)
            return jsonify(schema.dump(project)), 200
    return "There is no object with id="+pk, 404


@app.route("/projects")
def get_projects():
    schema = ProjectSchema(many=True)
    projects = schema.dump(all_projects)
    return jsonify(projects), 200


@ app.route('/projects', methods=['POST'])
def add_project():
    schema = ProjectSchema(many=False)
    project = ProjectSchema().load(request.get_json())
    newProject = Project(project["description"], project["requirements"],
                         project["max_budget"], project["bids_deadline"], project["owner"])
    all_projects.append(newProject)
    return jsonify(schema.dump(newProject)), 200


@ app.route('/offer', methods=['POST'])
def bid_to_project():
    offer = OfferSchema().load(request.get_json())
    for project in all_projects:
        print(project.id)
        print(offer.project_id)
        if str(project.id) == str(offer.project_id):
            project.assign_better_offer(offer)
            return request.get_json(), 200
    return "There is no object with id = "+str(offer.project_id), 404
