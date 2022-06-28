import sys
input = sys.stdin.readline
from itertools import permutations

n, m = map(int, input().split())
list_n = []
for i in range(1, n+1):
    list_n.append(i)
com = list(permutations(list_n, m))
for i in com:
    print(' '.join(map(str, i)))