import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement

num = int(input())
roma = [1, 5, 10, 50]
com = list(combinations_with_replacement(roma, num))
result = []
for i in com:
    result.append(sum(i))
result = set(result)
print(len(result))