import sys
from collections import deque
input = sys.stdin.readline

dummies = []
is_sorted = True
n, m = tuple(map(int, input().split()))
for _ in range(m):
    k = int(input())
    tmp = list(map(int, input().split()))
    for i in range(1, k):
        if tmp[i] > tmp[i-1]:
            is_sorted = False
            break
    if not is_sorted:
        break

print("No" if not is_sorted else "Yes")
            
    # dummies.append(list(map(int, input().split())))

# def solution(dummies):
#     book_num = 1
#     while book_num < n:
#         is_poped = False
#         for i in range(m):
#             if len(dummies[i]) > 0 and dummies[i][-1] == book_num:
#                 dummies[i].pop()
#                 is_poped = True
#                 book_num += 1
#         if not is_poped:
#             return "No"
#     return "Yes"

# print(solution(dummies))