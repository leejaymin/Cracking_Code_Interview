import sys
import string

s = input().strip()

sl = list(s)

i = 0
count = 1
while i < len(sl):
    if sl[i].isupper():
        count += 1
    i += 1

print(count)
