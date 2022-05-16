from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())   # n: 큐의 크기, m: 뽑아내려는 원소 개수
spot = deque(list(map(int, input().split())))   # 뽑아내려는 원소 위치

inx = deque(list(range(n)))   # 기존 인덱스
cnt = 0
for i in range(m):
    while True:
        if inx.index(spot[i] - 1) <= len(inx)//2:
            if inx[0] == spot[i] - 1:
                inx.popleft()
                break
            else:
                inx.append(inx.popleft())
                cnt += 1
        else:
            if inx[0] == spot[i] - 1:
                inx.popleft()
                break
            else:
                inx.appendleft(inx.pop())
                cnt += 1

print(cnt)
