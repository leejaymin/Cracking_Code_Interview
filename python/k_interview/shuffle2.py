import os
import random


def FisherYatesShuffle(data):
    number =  random.randint(0, len(data)-1)
    item = data.pop(number)
    return item, data


def randomRange(numPlaylist):
    # Compute rangee
    index = int(numPlaylist * random.randint(20, 30) / 100)
    return index


#print(os.getcwd())
f = open("input000.txt","r")
#f = open("./k_interview/input000.txt","r")
t = int(f.readline())
for a0 in range(t):
    playlist = list(map(str, f.readline().strip().split('\t')))
    artist = list(map(str, f.readline().strip().split('\t')))
    numPlaylist = len(artist)
    output = [[] for _ in range(numPlaylist)]


    tupleList = list(zip(artist, playlist))
    dic = dict([(key, []) for key in set(artist)])
    dicOffset = dict([(key, []) for key in set(artist)])
    for line in tupleList:
        dic[line[0]].append(line[1])
    #print(dic)

    # set offset
    #offsetIndex = list(range(numPlaylist))
    #for artName in dicOffset.keys():
    #    item, offsetIndex  = FisherYatesShuffle(offsetIndex)
    #    dicOffset[artName] = item

    #print(dicOffset)

    # search space management
    searchSpace = [i for i in range(numPlaylist)]

    # Locating algorithm
    outputIndex = 0
    for artIndex in dic.keys():  # artist
        outputIndex, searchSpace = FisherYatesShuffle(searchSpace) # init offset

        for song in dic[artIndex]:  # to get song from list
            # empty check
            if len(output[outputIndex]) == 0:
                output[outputIndex] = song

                if outputIndex in searchSpace:
                    del searchSpace[searchSpace.index(outputIndex)] # reduce search space
            else:
                while True:
                    outputIndex = (outputIndex + 1) % len(searchSpace)
                    if len(output[outputIndex]) == 0:
                        output[outputIndex] = song
                        del searchSpace[searchSpace.index(outputIndex)]  # reduce search space
                        break
            # increase 20~30% interval range
            outputIndex = (outputIndex + randomRange(len(searchSpace))) % len(searchSpace)

    print("OK")
    # print tab-based
    print(*output, sep='\t')









