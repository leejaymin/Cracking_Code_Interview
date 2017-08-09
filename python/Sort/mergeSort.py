import random

# Time Complexity O(nLogn)
# Space Complexity O(n)

def recursiveMergeSort(A):

    ### Base case ###
    if len(A) <= 1:
        return A

    ### A를 반으로 쪼개서 recursive call을 해 주고 정렬된 반쪽짜리들을 받아옵니다.
    left = recursiveMergeSort(A[:int(len(A)/2)])
    right = recursiveMergeSort(A[int(len(A)/2):])

    ### 여기서부터 두 개의 쪼개졌던 list를 합치는 Merge 부분입니다.
    ### 여기서 포인트는 정렬된 상태로 돌아왔기 때문에 앞에서부터 순차적으로 한번만 돌면 정렬시킬 수 있다는 것입니다.
    i, j, k = 0, 0, 0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    if i == len(left): #만약 left의 원소를 모두 채웠고, right가 남아있을 때.
        while j<len(right):
            A[k] = right[j]
            j += 1
            k += 1
    elif j == len(right): #만약 right의 원소를 모두 채웠고, left가 남아있을 때.
        while i<len(left):
            A[k] = left[i]
            i += 1
            k += 1
    return A #마지막으로 정렬된 list를 리턴합니다.

# to memorize
def recursiveMergeSort2(A):
    if len(A) <= 1:
        return A

    left = recursiveMergeSort2(A[:int(len(A)/2)])
    right = recursiveMergeSort2(A[int(len(A)/2):])

    merge = [[] for _ in range(len(left)+len(right))]
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merge[k] = left[i]
            i += 1
        else:
            merge[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        merge[k:] = right[j:]
    else:
        merge[k:] = left[i:]

    return merge

if __name__ == "__main__":

    A = [random.randint(1,100) for _ in range(10)]
    print("unsorted List:")
    print(A)
    print("Sorted List:")
    print(recursiveMergeSort(A))
    random.shuffle(A)
    print(A)
    print(recursiveMergeSort2(A))
