def calc(i):
    length = 255
    for dx in [-2, -1, 1, 2]:
        x = i + dx
        if 0 <= x < num:
            if building[i] > building[x]:
                length = min(length, building[i] - building[x])
            else:
                return False
    return length

for k in range(10):
    num = int(input())
    building = list(map(int, input().split()))
    cnt = 0
    for i in range(2, num-2):
        rest = calc(i)
        if rest:
            cnt += rest
    print(f'#{k+1} {cnt}')
