from flask import Flask, jsonify
from resources.user import user
import models

DEBUG = True
PORT = 8000

app = Flask(__name__) 

app.register_blueprint(user, url_prefix='/api/v1/user')

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
