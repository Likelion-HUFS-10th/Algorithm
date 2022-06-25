import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
a = [(i - k) for i in a]
temp = []
cnt = 0

def solve(weight):
	global cnt 

	if weight < 500:
		return

	if len(temp) == n:
		cnt += 1
		return 
	
	for i in range(1, n+1):
		if not i in temp:
			temp.append(i)
			solve(weight + a[i-1])
			temp.pop()

solve(500)
print(cnt)

