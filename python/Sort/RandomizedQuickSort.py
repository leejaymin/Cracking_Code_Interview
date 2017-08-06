import random

# 먼저 자주 쓰이는 list내 swap을 해주는 함수를 선언합니다.
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# 아까 말씀드렸다시피, pivot을 선택한 후에(parition 함수의 결과값으로 pivot의 최종 index가 나옵니다.) recursive call로 쪼갭니다.
def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p - 1)
        quicksort(A, p + 1, hi)


# 이제 pivot을 뽑는 과정을 알아봅시다.
def partition(A, lo, hi):
    import random
    pivotIndex = random.randint(lo, hi)  ##pivot을 뽑기로 뽑습니다.
    pivotValue = A[pivotIndex]

    # 일단 pivot을 마지막 원소와 바꾸고,
    swap(A, pivotIndex, hi)

    storeIndex = lo
    # 나머지 원소들은 A[hi]와 비교하면서 재정렬합니다.
    for i in range(lo, hi):
        if A[i] < pivotValue:
            swap(A, i, storeIndex)
            storeIndex += 1
    swap(A, storeIndex, hi)  # 마지막으로 pivot을 자신보다 큰 원소들의 첫번째 원소와 바꿔줍니다. (전반부, 후반부를 나누기 위해서)
    return storeIndex

if __name__ == "__main__":
    A = [random.randint(0, 100) for _ in range(15)]  # 임의로 0~100까지 15개 수를 뽑습니다.
    print(A)
    quicksort(A, 0, len(A)-1)
    print(A)