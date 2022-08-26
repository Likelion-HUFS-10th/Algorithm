n, m = map(int, input().split())
rc = list(map(int, input().split()))

def func1(s, e):
    total = 0
    if s > e:
        return
    mid = (s + e) // 2
    for r in rc:
        if r > mid:
            total += (r - mid)
    if total == m:
        return mid
    elif total > m:
        return func1(mid+1, e)
    else:
        return func1(s, mid-1)

print(func1(0, max(rc)))