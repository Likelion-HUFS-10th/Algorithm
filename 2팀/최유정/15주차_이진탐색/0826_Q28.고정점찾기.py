n = int(input())
nlist = list(map(int, input().split()))

def func1(s, e):
    if s > e or nlist[s] > n-1 or nlist[e] < 0:
        return -1
    mid = (s + e) // 2
    if nlist[mid] == mid:
        return mid
    elif nlist[mid] > mid:
        return func1(s, mid-1)
    else:
        return func1(mid+1, e)

print(func1(0, n-1))