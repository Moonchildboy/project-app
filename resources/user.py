import models

from flask import Blueprint

user = Blueprint('user', 'user')

@user.route('/<id>',methods=['GET'])
def get_user(id):
	return "users"