import sys
input = sys.stdin.readline

n, m = map(int, input().split())
balls = list(map(int, input().split()))

result = [0] * (m+1)
cnt = 0

for weight in balls:
	result[weight] += 1 

for i in range(1, m+1):
	n -= result[i]
	cnt += n * result[i]

print(cnt)

"""import sys
input = sys.stdin.readline

n, m = map(int, input().split())
balls = list(map(int, input().split()))
cnt = 0

for i in range(n):
	w = balls[i]

	ea = balls[i+1::].count(w)
	cnt += n - (i + 1) - ea

print(cnt)
"""