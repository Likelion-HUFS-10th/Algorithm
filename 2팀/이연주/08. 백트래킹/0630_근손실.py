from itertools import permutations
n, k = map(int, input().split())
a = list(map(int, input().split()))

candidate = list(permutations(a, n))
cnt = 0
for candi in candidate:
    current = 500
    possible = True
    for today in candi:
        current = current + today - k
        if current < 500:
            possible = False
            break
    if possible:
        cnt += 1

print(cnt)