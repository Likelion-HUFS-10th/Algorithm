from itertools import combinations

n, m = map(int, input().split())
ball = list(map(int, input().split()))
cnt = 0

total = len(list(combinations(ball, 2)))

for i in range(1, m+1):
    if ball.count(i) > 1:
        cnt += len(list(combinations(range(ball.count(i)), 2)))
total -= cnt
print(total)