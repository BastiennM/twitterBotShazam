from ShazamAPI import Shazam
import json

mp3_file_content_to_recognize = open('daddy.mp3', 'rb').read()

shazam = Shazam(mp3_file_content_to_recognize)
recognize_generator = shazam.recognizeSong()
#while True:
# print(recognize_generator) # current offset & shazam response to recognize requests
listrecognize = list(recognize_generator)
print("--------------------")
print(listrecognize[0][1]["track"]["title"]) #GET part TITLE OF THE SONG
print(listrecognize[0][1]["track"]["subtitle"]) #GET part subtitle OF THE SONG
print(listrecognize[0][1]["track"]["images"]["coverarthq"]) #GET cover OF THE SONG
print(listrecognize[0][1]["track"]["share"]["subject"]) #GET complete title OF THE SONG
print(listrecognize[0][1]["track"]["share"]["href"]) #GET link to the shazam page
print(listrecognize[0][1]["track"]["hub"]["options"][0]["actions"][0]['uri']) #GET link to the applemusic page
print(listrecognize[0][1]["track"]["hub"]["providers"][0]["actions"][0]['uri']) #GET spotify search (ex : http://open.spotify.com/search/only+happy+when+it+rains)
print(listrecognize[0][1]["track"]["hub"]["providers"][1]["actions"][0]['uri']) #GET deezer search (ex : https://www.deezer.com/search/daddy%20sdm)
print(listrecognize[0][1]["track"]["sections"][0]["metadata"][0]["text"]) #GET album name
print(listrecognize[0][1]["track"]["sections"][0]["metadata"][1]["text"]) #GET album maison de disque name
print(listrecognize[0][1]["track"]["sections"][0]["metadata"][2]["text"]) #GET album years
print(listrecognize[0][1]["track"]["sections"][0]["metadata"][2]["text"]) #GET album years
print("--------------------")
 
# with open('data.txt', 'wb') as file:
#     data = json.dumps(next(recognize_generator)).encode('utf-8')
#     file.write(data)
