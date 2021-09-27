from ShazamAPI import Shazam
import json
import requests
from datetime import datetime
import random
from subprocess import call

#create the url
url = str(random.randint(0,9999))

now = datetime.now().time()
print("start =", now)

mp3_file_content_to_recognize = open('mp3/daddyshort.mp3', 'rb').read()

shazam = Shazam(mp3_file_content_to_recognize)
recognize_generator = shazam.recognizeSong()
listrecognize = list(recognize_generator)

# request to get the youtube link
urlytb = listrecognize[0][1]["track"]["sections"][2]['youtubeurl']
payload={}
files={}
headers = {}
response = requests.request("GET", urlytb, headers=headers, data=payload, files=files)
jsonedytb = response.json()

#create dict for element
item = dict(
    titlepart= (listrecognize[0][1]["track"]["title"]),  #GET part TITLE OF THE SONG
    subtitle=(listrecognize[0][1]["track"]["subtitle"]), #GET part subtitle OF THE SONG
    cover=(listrecognize[0][1]["track"]["images"]["coverarthq"]), #GET cover OF THE SONG
    completetitle=(listrecognize[0][1]["track"]["share"]["subject"]), #GET complete title OF THE SONG
    shazamlink=(listrecognize[0][1]["track"]["share"]["href"]), #GET link to the shazam page
    applemusiclink = (listrecognize[0][1]["track"]["hub"]["options"][0]["actions"][0]['uri']), #GET link to the applemusic page
    spotifysearch = (listrecognize[0][1]["track"]["hub"]["providers"][0]["actions"][0]['uri']), #GET spotify search (ex : http://open.spotify.com/search/only+happy+when+it+rains)
    deezersearch = (listrecognize[0][1]["track"]["hub"]["providers"][1]["actions"][0]['uri']), #GET deezer search (ex : https://www.deezer.com/search/daddy%20sdm)
    albumname=(listrecognize[0][1]["track"]["sections"][0]["metadata"][0]["text"]), #GET album name
    albumid=(listrecognize[0][1]["track"]["albumadamid"]), #GET album id 
    disqueeditor = (listrecognize[0][1]["track"]["sections"][0]["metadata"][1]["text"]), #GET album maison de disque name
    year = (listrecognize[0][1]["track"]["sections"][0]["metadata"][2]["text"]), #GET album years
    youtubelink = (jsonedytb['actions'][0]['uri']) # get youtube link
    )

#create dict for lyrics
newlyrics = dict(
    lyrics = (listrecognize[0][1]["track"]["sections"][1]["text"]) #get lyrics
    )

#request to get the spotify link
#delete a part of string with "spotify:search:"
s = (listrecognize[0][1]["track"]["hub"]["providers"][0]["actions"][0]['uri'])
string = s.replace("spotify:search:", "")

#delete the quote from string
newstring = string.replace('"','')

urlspot = "https://api.spotify.com/v1/search?q="+newstring+"&type=track&limit=1"
payload={}
files={}
headers = {
  'Authorization': 'Bearer A REMPLIR',
}
response = requests.request("GET", urlspot, headers=headers, data=payload, files=files)
jsonedspotify = response.json()

#create dict for spotify
itemspotify = dict(
    artistpage = jsonedspotify['tracks']["items"][0]['artists'][0]['external_urls']['spotify'], # get the artist page
    artistid = jsonedspotify['tracks']["items"][0]['artists'][0]['id'], # get the artist id
    trackpage = jsonedspotify['tracks']["items"][0]['external_urls']['spotify'], # get the track page
    trackid = jsonedspotify['tracks']["items"][0]['id'], # get the track id
    albumpage =jsonedspotify['tracks']["items"][0]['album']['external_urls']['spotify'], # get the album page
    albumid=jsonedspotify['tracks']["items"][0]['album']['id'] # get the album id
)

# create all json files
with open("json/spotify"+url+".json", "w") as file_object:
    json.dump(itemspotify, file_object)
with open("json/datanew"+url+".json", "w") as file_object:
    json.dump(item, file_object)
with open("json/lyrics"+url+".json", "w") as file_objects:
    json.dump(newlyrics, file_objects)

#send by ssh the json files
cmd = 'scp /home/pi/botShazam/twitterBotShazam/json/datanew'+url+'.json u105060309@access875183491.webspace-data.io:/kunden/homepages/16/d875183491/htdocs/shazambot/json'
call(cmd.split())
cmd = 'scp /home/pi/botShazam/twitterBotShazam/json/lyrics'+url+'.json u105060309@access875183491.webspace-data.io:/kunden/homepages/16/d875183491/htdocs/shazambot/json'
call(cmd.split())
cmd = 'scp /home/pi/botShazam/twitterBotShazam/json/spotify'+url+'.json u105060309@access875183491.webspace-data.io:/kunden/homepages/16/d875183491/htdocs/shazambot/json'
call(cmd.split())

now = datetime.now().time()
print('send =',now)
print('your url is bastiendev.fr/?url='+url)
