import requests
from secrets import GM_API_KEY

uri_place_details = "https://maps.googleapis.com/maps/api/place/details/json?place_id="

place_id = "ChIJt_cTCjWHj4ARXGHUHr_Jt6Y"


# print(url)
# print(response.text)
# with open("place_from_id1.txt", "w") as f:
#     f.write(response.text)

def gm_id_query(place_id):
    payload = {}
    headers = {}
    url = uri_place_details + place_id + GM_API_KEY
    response = requests.request("GET", url, headers=headers, data=payload)
    with open("place_from_id1.txt", "w") as f:
        response=response
        f.write(response.text)
    return get_uri_from_response(response)

def get_uri_from_response(response):
    """Takes response and outputs place url"""
    ind_loc = response.text.rfind("url")
    ind_lis1 = response.text[ind_loc:].split(":")
    ind_lis2 = (ind_lis1[1] + ":" + ind_lis1[2]).split(",")
    ind_lis3 = ind_lis2[0]
    return ind_lis3
