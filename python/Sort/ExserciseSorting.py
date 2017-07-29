
def mergeSort(A):

    left = mergeSort(A[0:int(len(A)/2)])
    right = mergeSort(A[int(len(A)/2):len(A)])

    return A

if __name__ == "__main__":

    A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("unsorted List:")
    print(A)
    print("Sorted List:")
    print(mergeSort(A))