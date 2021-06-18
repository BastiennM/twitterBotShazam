from ShazamAPI import Shazam
import json
import requests
from datetime import datetime

now = datetime.now().time()
print("start =", now)

mp3_file_content_to_recognize = open('mp3/testshort.mp3', 'rb').read()

shazam = Shazam(mp3_file_content_to_recognize)
recognize_generator = shazam.recognizeSong()
listrecognize = list(recognize_generator)
now = datetime.now().time()
print('finish list =', now)

# request to get the youtube link
url = "https://cdn.shazam.com/video/v3/-/RU/iphone/561541479/youtube/video?q=SDM+%22Daddy%22"
payload={}
files={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload, files=files)
jsonedytb = response.json()

now = datetime.now().time()
print('finish request ytb =',now)

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

newlyrics = dict(
    lyrics = (listrecognize[0][1]["track"]["sections"][1]["text"]) #get lyrics
    )

now = datetime.now().time()
print('finish dict =',now)

with open("json/datanew.json", "w") as file_object:
    json.dump(item, file_object)
with open("json/lyrics.json", "w") as file_objects:
    json.dump(newlyrics, file_objects)

now = datetime.now().time()
print('success =',now)

from subprocess import call
cmd = 'scp /home/pi/botShazam/twitterBotShazam/json/datanew.json u105060309@access875183491.webspace-data.io:/kunden/homepages/16/d875183491/htdocs/shazambot'
call(cmd.split())
cmd = 'scp /home/pi/botShazam/twitterBotShazam/json/lyrics.json u105060309@access875183491.webspace-data.io:/kunden/homepages/16/d875183491/htdocs/shazambot'
call(cmd.split())

now = datetime.now().time()
print('send =',now)
