import requests
from secrets import GM_API_KEY

uri_base1 = "https://maps.googleapis.com/maps/api/place/findplacefromtext/"
uri_base2 = "https://maps.googleapis.com/maps/api/place/textsearch/"

endpoint = "json?query=restaurants%20in%20Sydney&key=" + GM_API_KEY

payload = {}
headers = {}

url = uri_base2 + endpoint

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
with open("response.txt", "w") as f:
    f.write(response.text)
