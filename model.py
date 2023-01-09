"""Models and database functions for scoothub App"""
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
engine = create_engine('sqlite:///:scoothub:', echo=True)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///scoothub'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy()
db.app = app
#######################


class Device(db.Model):
	"""Device Table for scoothub"""

	__tablename__ = "devices"

	device_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	event_id = db.Column(db.String(64), nullable=True)
	type = db.Column(db.String(200), nullable=True)
	address = db.Column(db.String(1028), nullable=True)
	lat = db.Column(db.String(200), nullable=True)
	lon = db.Column(db.String(200), nullable=True)
	city = db.Column(db.String(200), nullable=True)
	state = db.Column(db.String(200), nullable=True)
	status = db.Column(db.String(200), nullable=True)
	charge = db.Column(db.String(200), nullable=True)

	def __repr__(self):
		"""Provide helpful representation when printed."""
		return "<device_id={} event_id={} type={} address={} lat={} lon={} city={} state={} status={} charge={}>".format(
			self.device_id, self.event_id, self.type, self.address, self.lat, self.lon, self.city, self.state, self.statis, self.charge)


class Event(db.Model):
	"""Scoothub download events"""

	__tablename__ = "user_log"

	event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	source_id = db.Column(db.Integer, db.ForeignKey('sources.source_id'))
	datetime = db.Column(db.DateTime, nullable=True)
	time = db.Column(db.Time, nullable=True)
	city = db.Column(db.String(200), nullable=True)
	state = db.Column(db.String(200), nullable=True)

	def __repr__(self):
		"""Provide helpful representation when printed."""
		return "<event_id={} source_id={} datetime={} time={} city={} state={}>".format(
			self.event_id, self.source_id, self.datetime, self.time, self.city, self.state)



class Source(db.Model):
	"""scoothub sources"""

	__tablename__ = "sources"

	source_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String(96))
	login_un = db.Column(db.String(96), nullable=True)
	login_pass = db.Column(db.String(96), nullable=True)
	url = db.Column(db.String(96), nullable=True)
	endpoint = db.Column(db.String(96), nullable=True)
	notes = db.Column(db.String(1028), nullable=True)

	def __repr__(self):
		"""Provide helpful representation when printed."""
		return "<source_id={} name={} login_un={} login_pass={} url={} endpoint={} notes={}>".format(
			self.source_id, self.name, self.login_un, self.login_pass, self.url, self.endpoint, self.notes)


################################################################################
# Helper functions

def connect_to_db(app, db_uri='postgresql:///scoothub'):
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
	connect_to_db(app, 'postgresql:///scoothub')
	print("Connected to DB.")
