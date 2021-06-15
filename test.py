from ShazamAPI import Shazam
import json

mp3_file_content_to_recognize = open('test.mp3', 'rb').read()

shazam = Shazam(mp3_file_content_to_recognize)
recognize_generator = shazam.recognizeSong()
listrecognize = list(recognize_generator)

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
    disqueeditor = (listrecognize[0][1]["track"]["sections"][0]["metadata"][1]["text"]), #GET album maison de disque name
    year = (listrecognize[0][1]["track"]["sections"][0]["metadata"][2]["text"]), #GET album years
    lyrics = (listrecognize[0][1]["track"]["sections"][1]["text"]) #get lyrics
    )

with open("data.json", "w") as file_object:
    json.dump(item, file_object)

