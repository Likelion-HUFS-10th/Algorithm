import sys
input = sys.stdin.readline

n = int(input())   # 점의 개수
dot = [tuple(map(int, input().split())) for _ in range(n)]

dot = sorted(dot, key=lambda x: (x[0], x[1]))

for i in range(n):
    print(dot[i][0], dot[i][1])
