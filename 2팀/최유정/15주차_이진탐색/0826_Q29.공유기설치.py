import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()
opt = 0

def func1(s, e):
    global opt
    standard = house[0]
    if s > e:
        return opt
    mid = (s + e) // 2
    cnt = 1
    for h in house:
        if h >= standard + mid:
            standard = h
            cnt += 1
    if cnt >= c:
        opt = mid
        return func1(mid+1, e)
    else:
        return func1(s, mid-1)
    
print(func1(1, house[n-1]-house[0]))