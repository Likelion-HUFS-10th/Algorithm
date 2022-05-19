import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
a = list(map(int, input().split()))
cut_a = a[:]
cut_a = deque(cut_a)
result = []

for _ in range(v - 1):
    cut_a.popleft()

for _ in range(m):
    question = int(input())
    if question < n:
        result.append(a[question])
    else:
        question -= v - 1
        question = question % len(cut_a)
        result.append(cut_a[question])

for answer in result:
    print(answer)