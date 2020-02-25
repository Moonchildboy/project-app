from flask import Flask, jsonify, g
from flask_login import LoginManager
from resources.user import user
import models

DEBUG = True
PORT = 8000

app = Flask(__name__) 

app.secret_key = "Help is quatum"

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
	try:
		return models.User.get(models.User.id == userid)
	except models.DoesNotExist:
		return None


app.register_blueprint(user, url_prefix='/api/v1/user')


if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
