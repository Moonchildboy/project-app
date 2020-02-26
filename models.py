import datetime # to be use for start stop columns
from peewee import *

from flask_login import UserMixin

DATABASE = SqliteDatabase('projects.sqlite')

class User(UserMixin, Model): 
	username=CharField(unique=True)
	email=CharField(unique=True)
	password=CharField()#should this include unique=True 

	class Meta:
		database = DATABASE

class Project(Model): 
	title=CharField()
	start_date=DateField() #perhaps include [ choices = None ] arg with suitable value
	end_date=DateField() #include arg to represent optionality
	status=CharField()
	priority=CharField()
	user=ForeignKeyField(User, backref='project') #why did we have this at the User level in wF's?

	# category=CharField() <--include at a later date

	class Meta:
		database = DATABASE

class Goal(Model):
	title=CharField()
	project=ForeignKeyField(Project, backref='goal')#not sure if I'm doing this right

	class Meta:
		database = DATABASE

class Task(Model):
	title=CharField()
	complete=BooleanField(default=False)
	start_time=TimeField()#<-- to be changed in state
	end_time=TimeField()#<-- to be changed in state
	goal=ForeignKeyField(Goal, backref='goal')#not sure if I'm doing this right

	class Meta:
		database = DATABASE


def initialize(): # NOTE we are making this name up
  DATABASE.connect() # analogous to mongoose.connect(...)

  DATABASE.create_tables([User, Project], safe=True)
  print("Connected to DB and created tables if they weren't already there")

  DATABASE.close()