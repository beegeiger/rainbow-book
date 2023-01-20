import requests
from place_id_query import gm_id_query
from place_name_query import gm_place_query

locations_rb = Blueprint('locations_rb', __name__, template_folder='../Static/templates',
    static_folder='../Static')

@locations_rb("/loc_lookup", methods=["GET"])
def find_loc(place_uri):
    """Takes a Google Maps Place URI and looks up the google place_id"""
    return place_id
