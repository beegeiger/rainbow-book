"""Models and database functions for rainbowbook App"""
from flask import jsonify, Flask
import datetime
from datetime import datetime
import json
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, Unicode, inspect, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_debugtoolbar import DebugToolbarExtension

# from server import app

# Required to use Flask sessions and the debug toolbar
engine = create_engine('sqlite:///:rainbowbook:', echo=True)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///rainbowbook'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy()
db.app = app
#######################


class Location(db.Model):
	"""Locations Table for rainbowbook"""

	__tablename__ = "locations"

	location_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	type = db.Column(db.String(200), nullable=True)
	address = db.Column(db.String(1028), nullable=True)
	lat = db.Column(db.String(200), nullable=True)
	lon = db.Column(db.String(200), nullable=True)
	city = db.Column(db.String(200), nullable=True)
	state = db.Column(db.String(200), nullable=True)
	status = db.Column(db.String(200), nullable=True)
	charge = db.Column(db.String(200), nullable=True)
	rating_value = db.Column(db.Integer, nullable=True)
	rating_number = db.Column(db.Integer, nullable=True)
	api_id = db.Column(db.String(200), nullable=True)
	link = db.Column(db.String(200), nullable=True)
	attributes = db.Column(db.JSON, nullable=True)

	def __repr__(self):
		"""Provide helpful representation when printed."""
		return "<device_id={} type={} address={} lat={} lon={} city={} state={} status={} charge={} rating_value={} rating_number={} api_id={} link={} attributes={}>".format(
			self.device_id, self.type, self.address, self.lat, self.lon, self.city, self.state, self.statis, self.charge, self.rating_value, self.rating_number, self.api_id, self.link, self.attributes)


class Review(db.Model):
	"""rainbowbook reviews"""

	__tablename__ = "user_log"

	review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
	datetime = db.Column(db.DateTime, nullable=True)
	review_value = db.Column(db.Integer, nullable=True)
	review_text = db.Column(db.String(200), nullable=True)

	def __repr__(self):
		"""Provide helpful representation when printed."""
		return "<review_id={} location_id={} user_id={} datetime={} review_value={} review_text={}>".format(
			self.review_id, self.location_id, self.user_id, self.datetime, self.review_value, self.review_text)

class User(db.Model):
	"""User Table in rainbowbook App"""

	__tablename__ = "users"

	user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	username = db.Column(db.String(64), nullable=True)
	name = db.Column(db.String(64), nullable=True)
	fname = db.Column(db.String(64), nullable=True)
	lname = db.Column(db.String(64), nullable=True)
	email = db.Column(db.String(256))
	created_at = db.Column(db.DateTime, nullable=True)
	phone = db.Column(db.String(28), nullable=True)

	def __repr__(self):
		"""Provide helpful representation when printed."""
		return "<user_id={} username={} name={} fname={} lname={} email={} created_at={} phone={} type={}>".format(
			self.user_id, self.username, self.name, self.fname, self.lname, self.email,self.created_at, self.phone, self.type)

################################################################################
# Helper functions

def connect_to_db(app, db_uri='postgresql:///rainbowbook'):
	"""Connect the database to our Flask app."""
	# Configure to use our PstgreSQL database
	print("Connecting")
	# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	# db.app = app
	db.init_app(app)
	with app.app_context():
		db.drop_all()
		db.create_all()
		starter_data()

if __name__ == "__main__":
	connect_to_db(app, 'postgresql:///rainbowbook')
	print("Connected to DB.")
