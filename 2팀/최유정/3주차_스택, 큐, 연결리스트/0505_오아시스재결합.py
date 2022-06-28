#

import sys
input = sys.stdin.readline

def func1(n, line):
    global cnt
    for i in range(n-1):
        max = 0
        for j in range(i+1, n):
            if max <= line[j] and max < line[i]:
                max = line[j]
                cnt += 1
            elif max == line[j]:
                max = line[j]
                cnt += 1
    return cnt

n = int(input())
line = []
cnt = 0
for _ in range(n):
    height = int(input())
    line.append(height)
print(func1(n, line))