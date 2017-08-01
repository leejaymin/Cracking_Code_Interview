import sys
import codecs
import random

sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

def FisherYatesShuffle(data):
    number = random.randint(0, len(data) - 1)
    item = data.pop(number)
    return item, data

def randomRange(numPlaylist):
    # Compute rangee
    index = int(numPlaylist * random.randint(20, 30) / 100)
    return index


f = open("input000.txt", "r")
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
    # print(dic)

    # set offset
    offsetIndex = list(range(numPlaylist))
    for artName in dicOffset.keys():
        item, offsetIndex = FisherYatesShuffle(offsetIndex)
        dicOffset[artName] = item

    # print(dicOffset)


    # Locating algorithm
    outputIndex = 0
    for artIndex in dic.keys():  # artist
        outputIndex = dicOffset[artIndex]  # init offset

        for song in dic[artIndex]:  # to get song from list
            # empty check
            if len(output[outputIndex]) == 0:
                output[outputIndex] = song
            else:
                while True:
                    outputIndex = (outputIndex + 1) % numPlaylist
                    prev = (outputIndex - 1)  # time out ocuurs
                    nexv = (outputIndex + 1) % numPlaylist  # time out ocuurs
                    if len(output[outputIndex]) == 0 and output[prev] not in dic[artIndex] and output[nexv] not in dic[
                        artIndex]:
                        output[outputIndex] = song
                        break

            # increase 20~30% interval range
            outputIndex = (outputIndex + randomRange(numPlaylist)) % numPlaylist

    # print tab-based
    print(*output, sep='\t')