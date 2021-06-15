import json
import requests

#open json with data
with open('data.json', 'r') as handle:
    parsed = json.load(handle)
    s = json.dumps(parsed['spotifysearch'])

#delete a part of string with "spotify:search:"
string = s.replace("spotify:search:", "")

#delete the quote from string
newstring = string.replace('"','')

url = "https://api.spotify.com/v1/search?q="+newstring+"&type=track&limit=1"
payload={}
files={}
headers = {
  'Authorization': 'Bearer BQB2uZfZcwR-3FWSv4Z4Ws1z_VGqe_-9dYkwB74MSTv_2H76y5slTYGjafHr34KJFChySnQkezSppFGOTEJIGlUYu-1gkJyfjaowUSN_c37L_DB2_o5VdZK66rYk2trGr3XCfF0',
}
response = requests.request("GET", url, headers=headers, data=payload, files=files)
jsonedspotify = response.json()

item = dict(
    artistpage = jsonedspotify['tracks']["items"][0]['artists'][0]['external_urls']['spotify'], # get the artist page
    artistid = jsonedspotify['tracks']["items"][0]['artists'][0]['id'], # get the artist id
    trackpage = jsonedspotify['tracks']["items"][0]['external_urls']['spotify'], # get the track page
    trackid = jsonedspotify['tracks']["items"][0]['id'], # get the track id
    albumpage =jsonedspotify['tracks']["items"][0]['album']['external_urls']['spotify'], # get the album page
    albumid=jsonedspotify['tracks']["items"][0]['album']['id'] # get the album id
)

with open("spotify.json", "w") as file_object:
    json.dump(item, file_object)