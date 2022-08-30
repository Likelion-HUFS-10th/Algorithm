n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]

start = min(money)
end = sum(money)

cnt = 0

while start <= end:
    mid = (start + end) // 2
    today = mid
    cnt = 1
    for i in money:
        if today < i:
            today = mid
            cnt += 1
        today -= i

    if cnt > m or mid < max(money):
        start = mid + 1
    else:
        end = mid - 1
        total = mid

print(total)
