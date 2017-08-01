import os
import random


def FisherYatesShuffle(data):
    number =  random.randint(0, len(data)-1)
    return data.pop(number)

print(os.getcwd())
f = open("input000.txt","r")
#f = open("./k_interview/input000.txt","r")
t = int(f.readline())
for a0 in range(t):
    playlist = list(map(str, f.readline().strip().split('\t')))
    artist = list(map(str, f.readline().strip().split('\t')))
    numPlaylist = len(artist)
    output = [[] for _ in range(numPlaylist)]

    print(playlist)
    print(artist)

    tupleList = list(zip(artist,playlist))
    dic = dict([(key, []) for key in set(artist)])
    dicOffset = dict([(key, []) for key in set(artist)])
    for line in tupleList:
        dic[line[0]].append(line[1])
    print(dic)

    # set offset
    offsetIndex = list(range(numPlaylist))
    for artName in dicOffset.keys():
        i = FisherYatesShuffle(offsetIndex)
        dicOffset[artName] = i

    print(dicOffset)

    # Compute rangee
    index = int(numPlaylist * random.randint(20, 30) / 100)

f.close()