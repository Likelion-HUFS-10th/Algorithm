import sys
input = sys.stdin.readline

n = int(input())
stack = [int(input()) for _ in range(n)]

cnt = 1

def watch():
	global cnt
	strd = stack.pop()

	while stack:
		block = stack.pop()
		if strd < block:
			cnt += 1
			strd = block
		
	return cnt

print(watch())
