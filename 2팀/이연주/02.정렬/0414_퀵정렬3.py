import sys
sys.setrecursionlimit(100000)

N = int(input())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))
exist = 0

def quick_sort(start, end):
    global exist

    if exist == 1:
        return

    if start >= end : # 원소가 1개인 경우 종료
        return
    if arrA == arrB:
        exist = 1
        return 
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while(left <= end and arrA[left] <= arrA[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and arrA[right] >= arrA[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            arrA[right], arrA[pivot] = arrA[pivot], arrA[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            arrA[left], arrA[right] = arrA[right], arrA[left]
        if arrA == arrB:
            exist = 1
            return
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(start, right - 1)
    quick_sort(right + 1, end)

quick_sort(0, N-1)
print(exist)