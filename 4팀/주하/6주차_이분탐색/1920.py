'''
이분탐색으로 풀기

이분탐색 조건 : 배열 정렬

런타임 에러 발생

'''
import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()    # 이분탐색 조건 -> 배열이 정렬되어야 사용 가능

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

for i in m_list:
    left = 0
    right  = m-1
    while left <= right:
        mid = (left+right) // 2

        if n_list[mid] == i:
            print(1)
            break
        elif n_list[mid] > i:
            right = mid - 1
        elif n_list[mid] < i:
            left = mid + 1
        else:
            print(0)
            break

        if left > right:
            print(0)
            break



#----------------이분 탐색 x ---------------
# import sys

# n = int(sys.stdin.readline())
# n_list = list(map(int, sys.stdin.readline().split()))

# m = int(sys.stdin.readline())
# m_list = list(map(int, sys.stdin.readline().split()))


# for i in range(len(m_list)):
#     if n_list[i] <= m_list[i]:
#         print(1)
#     else:
#         print(0)
