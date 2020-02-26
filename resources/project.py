#should there be an app.py route that controls the landing page
import models

from flask import Blueprint, request, jsonify
from flask_login import current_user,login_required
from playhouse.shortcuts import model_to_dict

project =  Blueprint('project', 'project')


@project.route('/', methods=['POST'])

def create_project():
	payload = request.get_json()
	print("I'm in the right route!")
	project = models.Project.create(
		title=payload['title'],
		start_date=payload['start_date'],
		end_date=payload['end_date'],
		status=payload['status'],
		priority=payload['priority'],
		user=current_user.id
		)

	print(project.__dict__)

	project_dict=model_to_dict(project)
	# include a password pop after back referencing user
	return jsonify(
		data=project_dict,
		message="Successfully created a project",
		status=201
		), 201

# show will display an unactivated sheet, no change in rendering from show to edit. 

@project.route('/', methods=['GET']) #maybe I should have modeled the master sheet?
def show_project_list():
	print(current_user)
	project_to_dict=[model_to_dict(project) for project in current_user.project] #maybe I need to back ref current_user to tie create and show together
	return jsonify(
		data=project_to_dict,
		message="showing a project sheet",
		status=200
		), 200


# POST '/project/' -- create project
# GET '/project/categories' -- get list of the categories
# GET '/project/<category> <<-- get data about all the projects for a category including tasks
# PUT '/project/<id>' -- updating/changing project info
# DELETE '/<id>' -- delete project

# GET '/eisenhower' <<-- renders the eisenhower sheet
# GET '/projects' <<-- list of all projects in all categories (stretch)
