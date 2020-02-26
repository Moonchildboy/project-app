import models
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, LoginManager
from playhouse.shortcuts import model_to_dict


user = Blueprint('user', 'user')

@user.route('/register', methods=['POST']) #
def register():
	payload = request.get_json()
	print(payload)

	payload['email'] = payload['email'].lower()
	payload['username'] = payload['username'].lower()

	try:
		models.User.get(models.User.email == payload['email'])
		return jsonify (
			data={},
			message="a user with that email already exists", 
			status=401
			), 401
	except models.DoesNotExist:
		created_user=models.User.create(
			username=payload['username'],
			email=payload['email'],
			password=generate_password_hash(payload['password'])
			)
		login_user(created_user)
		user_dict = model_to_dict(created_user)
		print(user_dict)
		print(type(user_dict['password']))
		user_dict.pop('password')

		return jsonify(
			data=user_dict,
			message=f"successfully registered as {user_dict['email']}", 
			status=201
			), 201
#___________________________________________________________________________________________

@user.route('/login', methods=['POST'])
def login():
	payload=request.get_json()
	# remove the line about --> payload['email'] = payload['email'].lower()
	payload['username'] = payload['username'].lower()

	try:
		user = models.User.get(models.User.username == payload['username'])
		user_dict = model_to_dict(user)
		password_is_good = check_password_hash(user_dict['password'], payload['password'])

		if password_is_good:
			login_user(user)
			user_dict.pop('password')
			return jsonify(
				data=user_dict,
				message=f"Successfully logged in as {user_dict['username']}", 
				status=200
				), 200
		else: 
			return jsonify(
				data={},
				message="Try another password", 
				status=401
				), 401
	except models.DoesNotExist:
		return jsonify(
			data={}, 
			message="username or password is incorrect",
			# is there a way to tell the user exactly which is no good? 
			status=401
			), 401		
#___________________________________________________________________________________________

# @user.route('logged_in', methods=['GET'])
# def get_logged_in_user():
# 	if not current_user.is_authenticated:
# 		return jsonify(
# 			data={},
# 			message="No user is currently logged in",
# 			status=401
# 			), 401

#___________________________________________________________________________________________

@user.route('/logout', methods=['GET'])
def logout():
	logout_user()
	return jsonify(
		data={},
		message="Successfully logged out",
		status=200
		), 200
