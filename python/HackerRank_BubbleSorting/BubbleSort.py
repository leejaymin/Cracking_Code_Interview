
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


def bubbleSort2(n,a):
    swap = 0
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap += 1
        if swap == 0:
            break
        swap = 0
    return a

def optimized_bubble_sort(L):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                temp = L[i+1]
                L[i+1] = L[i]
                L[i] = temp
                swapped = True



if __name__ == "__main__":
    a = [5, 4, 3, 2, 1]
    #numSwap, sortedA = bubbleSort(len(a), a)

    #print(bubbleSort2(len(a), a))
    optimized_bubble_sort(a)
    print(a)
#    print("Array is sorted in %d swaps."%numSwap)
#    print("First Element: %d"%sortedA[0])
#    print("Last Element: %d"%sortedA[-1])

