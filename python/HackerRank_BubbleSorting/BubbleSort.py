
def bubbleSort(n, a):
    cumulatedNumSwap = 0
    for i in range(0, n):
        numSwap = 0
        for j in range(0, n-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                numSwap += 1
        cumulatedNumSwap += numSwap
        if numSwap == 0:
            break
    return cumulatedNumSwap, a

if __name__ == "__main__":
    a = [2, 1, 3, 1, 2]
    numSwap, sortedA = bubbleSort(len(a), a)

    print("Array is sorted in %d swaps."%numSwap)
    print("First Element: %d"%sortedA[0])
    print("Last Element: %d"%sortedA[-1])