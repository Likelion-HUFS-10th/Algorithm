scores = []
time = []
result = 0

n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] == 1:
        scores.append(a[1])
        time.append(a[2])
        time[-1] -= 1
        if time[-1] == 0:
            result += scores.pop()
            time.pop()
    else:
        if len(time) == 0:
            continue
        time[-1] -= 1
        if time[-1] == 0:
            result += scores.pop()
            time.pop()
print(result)
