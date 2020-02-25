import datetime # to be use for start stop columns
from peewee import *

from flask_login import UserMixin

DATABASE = SqliteDatabase('projects.sqlite')

class User(UserMixin, Model): 
	username=CharField(unique=True)
	email=CharField(unique=True)
	password=CharField()

	class Meta:
		database = DATABASE

def initialize(): # NOTE we are making this name up
  DATABASE.connect() # analogous to mongoose.connect(...)

  DATABASE.create_tables([User], safe=True)
  print("Connected to DB and created tables if they weren't already there")

  DATABASE.close()