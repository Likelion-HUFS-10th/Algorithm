# https://www.acmicpc.net/problem/14888
import sys
input = sys.stdin.readline
from itertools import permutations


n = int(input())
a = list(map(int, input().split()))
num = list(map(int, input().split()))
operator = {0:'+', 1:'-', 2:'*', 3:'/'}
oper = []
maxnum = -float('INF')
minnum = float('INF')
for i in range(4):
    for j in range(num[i]):
        oper.append(operator[i])
op_per = set()
for i in permutations(oper, n-1):
    total = a[0]
    for j in range(n-1):
        if i[j] == '+':
            total += a[j+1]
        if i[j] == '-':
            total -= a[j+1]
        if i[j] == '*':
            total *= a[j+1]
        if i[j] == '/':
            total = int(total / a[j+1])
    maxnum = max(maxnum, total)
    minnum = min(minnum, total)

print(maxnum)
print(minnum)