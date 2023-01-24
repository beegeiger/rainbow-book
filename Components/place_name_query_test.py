import requests
import re
from secrets import GM_API_KEY

uri_text_search = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="


test_loc = "https://www.google.com/maps/place/Alameda+County+Superior+Courthouse/@37.7969823,-122.2585934,16z/data=!4m8!1m2!3m1!2sAlameda+County+Superior+Courthouse!3m4!1s0x808f87350a13f7b7:0xa6b7c9bf1ed4615c!8m2!3d37.7996116!4d-122.2631207"

test_loc_list = test_loc.split("/")
loc_name = test_loc_list[5].replace("+", "%")
lat_lng = test_loc_list[6]. split(",")
lat = lat_lng[0][1:]
lng = "C" + lat_lng[1]


payload = {}
headers = {}

url = uri_text_search + loc_name  + GM_API_KEY

response = requests.request("GET", url, headers=headers, data=payload)

print(loc_name)
print(response.text)
ind_loc = response.text.find("place_id")
ind_lis1 = response.text[ind_loc:].split(":")
ind_lis2 = ind_lis1[1].split(",")
ind_lis3 = exec(ind_lis2[0])
print(ind_lis3, type(ind_lis3))

with open("place_to_id2.txt", "w") as f:
    f.write(response.text)
