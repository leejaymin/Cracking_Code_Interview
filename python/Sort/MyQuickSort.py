import random

# 아까 말씀드렸다시피, pivot을 선택한 후에(parition 함수의 결과값으로 pivot의 최종 index가 나옵니다.) recursive call로 쪼갭니다.
def quicksort(A, start, end):
    if start < end:
        p = partition(A, start, end)
        quicksort(A, start, p - 1)
        quicksort(A, p + 1, end)
    return A


# 이제 pivot을 뽑는 과정을 알아봅시다.
def partition(A, start, end):
    pivot = end
    wall = start
    # 나머지 원소들은 A[hi]와 비교하면서 재정렬합니다.
    for i in range(start, end):
        if A[i] < A[pivot]:
            #swap
            A[i], A[wall] = A[wall], A[i]
            wall += 1
    A[pivot], A[wall] = A[wall], A[pivot] # 마지막으로 pivot을 자신보다 큰 원소들의 첫번째 원소와 바꿔줍니다. (전반부, 후반부를 나누기 위해서)
    return wall

# test 1
def quicksort2(A, start, end):
    pass

# test 2
def partition2(A, start, end):
    pass

if __name__ == "__main__":
    A = [random.randint(0, 100) for _ in range(15)]  # 임의로 0~100까지 15개 수를 뽑습니다.
    print(A)
    print(quicksort(A, 0, len(A)-1))
    random.shuffle(A)
    print(A)
    print(quicksort2(A, 0, len(A)-1))