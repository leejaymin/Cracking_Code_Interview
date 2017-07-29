
input = [1,2,3,4,5,6,7,8,9,10]

target = 1
index = 0

min = 0
max = len(input) -1
mid = int(len(input)/2)

step = 1
while (target != input[mid]):
    if input[mid] < target:
        min = mid +1
    else:
        max = mid -1

    mid = int((max+min)/2)
    step +=1

print("target index: %d, steps: %d"%(mid, step))