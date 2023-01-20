import flask

import datetime
from jinja2 import StrictUndefined
from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify, Blueprint, send_file)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (update, asc, desc)
import requests
import logging

from functools import wraps
from os import environ as env
from werkzeug.exceptions import HTTPException
from dotenv import load_dotenv, find_dotenv

from auth import requires_auth

views_bp = Blueprint('views_rb', __name__, template_folder='../templates',
    static_folder='../static')

@views_bp.route("/", methods=["GET"])
def go_home():
    """Renders the rainbowbook homepage. (Tested)"""
    return render_template("homepage.html")
