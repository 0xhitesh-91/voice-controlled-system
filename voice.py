import os
import glob

ALL_SONGS = [] 
song = glob.glob("/home/rohit/Desktop/research paper/17_CI6B_17BCS1805_17BCS1732/Project file/myassis/*")
for i in song:
    ALL_SONGS.append(i)

print(ALL_SONGS)

song = ''
for i in ALL_SONGS:
    if 'spectre' in i.lower():
        song = str(i)
        print(song)

print(song)

