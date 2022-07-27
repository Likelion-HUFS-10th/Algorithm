import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
city = [
    list(map(int, input().split()))
    for _ in range(n)
]
chicken, house = [], []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append([i, j])
        if city[i][j] == 1:
            house.append([i, j])
chic_c = list(combinations(chicken, m))
result = []

def func1():
    for c in chic_c:
        hap = 0
        for h in house:
            hap += check(h, c)
        result.append(hap)
    result.sort()
    return result[0]
            

def check(h, c):
    dis = float('INF')
    for chicken in c:
        dis = min(abs(chicken[0]-h[0]) + abs(chicken[1]-h[1]), dis)
    return dis

print(func1())