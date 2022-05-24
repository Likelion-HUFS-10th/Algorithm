"""
이분 탐색 > 정렬된 리스트에서 탐색 범위를 절반씩 좁혀가며 접근
함수 변수 > 시작점 , 끝점 받아줌
리스트를 정렬해주고 절반으로 나눴을때 타겟 값과 절반값을 비교하여 접근
"""

import sys
sys.setrecursionlimit(10**7) # 재귀 범위

N = int(input())
list_num = list(map(int, sys.stdin.readline().split()))
list_num.sort() # 리스트를 정렬

M = int(input())
find_num_list = list(map(int, sys.stdin.readline().split()))

def find_num(array, target, start, end):
    if start > end: # 없어서 계속 재귀함수 사용 -> start 값이 end보다 커지게 됨
        return 0

    mid = (start + end) // 2

    if array[mid] == target:
        return 1
    elif array[mid] > target: # 중간보다 작은 쪽에 있음
        return find_num(array, target, start, mid-1)
    elif array[mid] < target: # 중간보다 큰 쪽에 있음
        return find_num(array, target, mid+1, end)

for i in find_num_list:
    print(find_num(list_num, i, 0, len(list_num)-1))