
n = 3
a = [3,2,1]

cumulatedNumSwap = 0
for i in range(0,n):
    numSwap = 0
    for j in range(0,n-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            numSwap += 1
    cumulatedNumSwap += numSwap
    if numSwap == 0:
        break

print("Array is sorted in %d swaps."%cumulatedNumSwap)
print("First Element: %d"%a[0])
print("Last Element: %d"%a[n-1])