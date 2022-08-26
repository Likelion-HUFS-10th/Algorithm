import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
nlist.sort()
m = int(input())
mlist = list(map(int, input().split()))

def func1(s, e, i):
    if s > e:
        return False
    mid = (s + e) // 2
    if i == nlist[mid]:
        return True
    if i < nlist[mid]:
        return func1(s, mid-1, i)
    if i > nlist[mid]:
        return func1(mid+1, e, i)

for i in mlist:
    if func1(0, n-1, i):
        print("yes")
    else:
        print("no")