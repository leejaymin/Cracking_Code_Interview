
# my own Code
def mergeSort(A):
    if len(A) <= 1:
        return A

    # Divide = O(n)
    left = mergeSort(A[ :int(len(A)/2)])
    right = mergeSort(A[int(len(A)/2): ])

    # Merge
    i,j,k = 0,0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            A[k] = left[i]
            i += 1
            k += 1
        else:
            A[k] = right[j]
            j += 1
            k += 1

    # copy right data to sortedList
    if i == len(left):
        while j < len(right):
            A[k] = right[j]
            k += 1
            j += 1

    # copy left data to sortedList
    if j == len(right):
        while i < len(left):
            A[k] = left[i]
            k += 1
            i += 1

    return A

if __name__ == "__main__":
    A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("unsorted List:")
    print(A)
    print("Sorted List:")
    print(mergeSort(A))