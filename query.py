import requests
from secrets import GM_API_KEY

uri_find_place = "https://maps.googleapis.com/maps/api/place/findplacefromtext/"
uri_text_search = "https://maps.googleapis.com/maps/api/place/textsearch/"
uri_nearby_search = "https://maps.googleapis.com/maps/api/place/nearbysearch/"

endpoint = "json?query=restaurants%1in%1Sydney&key=" + GM_API_KEY
endpoint2 = "json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key=" + GM_API_KEY
endpoint3 = "json?location=37.7969823%2C-122.2585934&keyword=Courthouse&radius=1000&key=" + GM_API_KEY

test_loc = "https://www.google.com/maps/place/Alameda+County+Superior+Courthouse/@37.7969823,-122.2585934,16z/data=!4m8!1m2!3m1!2sAlameda+County+Superior+Courthouse!3m4!1s0x808f87350a13f7b7:0xa6b7c9bf1ed4615c!8m2!3d37.7996116!4d-122.2631207"
test_loc_list = test_loc.split("/")
loc_name = test_loc_list[5].replace("+", "%")
lat_lng = test_loc_list[6]. split(",")
lat = lat_lng[0][1:]
lng = "C" + lat_lng[1]


payload = {}
headers = {}

url = uri_nearby_search + endpoint3

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
with open("response6.txt", "w") as f:
    f.write(response.text)
