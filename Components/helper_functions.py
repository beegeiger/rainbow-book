import requests
from place_id_query import gm_id_query
from place_name_query import gm_place_query

def get_id_from_response(response):
    """Takes response and outputs place_id"""
    ind_loc = response.text.find("place_id")
    ind_lis1 = response.text[ind_loc:].split(":")
    ind_lis2 = ind_lis1[1].split(",")
    ind_lis3 = ind_lis2[0]
    return ind_lis3

def check_place_in_db(response):
    """Queries place_id in db. Outputs True if exists, False if new"""
    place_id = get_id_from_response(response)
    place = Location.query.filter(Location.place_id1 == place_id).all()
    if place == []:
        return "False"
    else:
        return "True"
