import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n, m = tuple(map(int, input().split()))
    q = deque(list(map(int, input().split())))
    cnt = 0
    while q:
        best = max(q)
        front = q.popleft()
        m -= 1

        if best == front:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            q.append(front)
            if m < 0:
                m = len(q)-1