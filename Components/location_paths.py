import requests
from place_id_query import gm_id_query
from place_name_query import gm_place_query

locations_rb = Blueprint('locations_rb', __name__, template_folder='../Static/templates',
    static_folder='../Static')

@locations_rb("/loc_id_lookup", methods=["GET"])
def find_place_id(place_uri):
    """Takes a Google Maps Place URI and looks up the google place_id"""
    gm_response = gm_place_query(place_uri)
    print(response)
    print(response.text)
    print(response.text.place_id)
    return response.text

@locations_rb("/place_lookup", methods=["GET"])
def loc_lookup(place_id):
    """Takes a Google Maps Place URI and looks up the google place_id"""
    gm_response = gm_id_query(place_id)
    print(response)
    print(response.text)
    print(response.text.place_id)
    return response.text
