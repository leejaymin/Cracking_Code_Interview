#!/bin/python3

import sys
import itertools

def IsAlternatingStr(s):
    LS = list(s)
    i = 0
    while i < len(LS)-1:
        if LS[i] == LS[i+1]:
            return False # violation
        else:
            i+=1
    return True

#s_len = int(input().strip())
s = input().strip()

uniqueStr = set(s)

for i in itertools.combinations(uniqueStr, 2):


print(IsAlternatingStr(s))


