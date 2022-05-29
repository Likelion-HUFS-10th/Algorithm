"""
이분탐색 사용x -> 시간초과 발생
마이너스 값에 대한 처리
"""
import sys
N,M = map(int, sys.stdin.readline().split())
tree_list = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(tree_list)

while start <= end:
    mid = (start + end) // 2
    sum_tree = 0
    for i in tree_list:
        if i >= mid:
            sum_tree += i - mid
    if sum_tree >= M:
        start = mid +1
    else:
        end = mid - 1

print(end)

# max_tree = max(tree_list) 
# for i in range(max_tree, 0, -1):
#     sum_tree = 0
#     for j in tree_list:
#         cut_tree = j - i
#         if cut_tree >= 0:
#             sum_tree += cut_tree
#     if sum_tree == M:
#         print(i)
#         break     