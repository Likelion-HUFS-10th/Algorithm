import sys
input = sys.stdin.readline

n, x = map(int, input().split())
nlist = list(map(int, input().split()))

def start(s, e, x):
    if s > e:
        return
    mid = (s + e) // 2
    if nlist[mid] == x and nlist[mid-1] != x:
        return mid
    elif nlist[mid] > x or nlist[mid-1] == x:
        return start(s, mid-1, x)
    else:
        return start(mid+1, e, x)

def end(s, e, x):
    if s > e:
        return
    mid = (s + e) // 2
    if nlist[mid] == x and nlist[mid+1] != x:
        return mid
    elif nlist[mid+1] == x:
        return end(mid+1, e, x)
    else:
        return end(s, mid-1, x)

if x not in set(nlist):
    print(-1)
else:
    start_index = start(0, n-1, x)
    end_index = end(start_index, n-1, x)
    print(end_index - start_index + 1)