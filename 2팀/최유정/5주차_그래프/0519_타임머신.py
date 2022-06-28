# 벨만 포드 알고리즘

import sys
input = sys.stdin.readline


def func1(bus):
    visited = [float('inf')] * (n+1)
    visited[1] = 0
    for i in bus:
        if visited[i[1]] > visited[i[0]]+i[2]:
            visited[i[1]] = visited[i[0]]+i[2]
    return visited
        
    

n, m = map(int, input().split())
bus = []
for _ in range(m):
    a, b, c = map(int, input().split())
    bus.append([a, b, c])

new_list = func1(bus)[2:]
for i  in new_list:
    if i <= 0:
        print(-1)
        sys.exit(0)


for i in new_list:
    if i == float('inf'):
        print(-1)
    else:
        print(i)