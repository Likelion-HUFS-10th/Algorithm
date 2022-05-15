import sys
input = sys.stdin.readline

n = int(input())
seniors = [int(input()) for _ in range(n) ]
cnt, member = 0, -1

def searching(idx):
	global cnt

	if temp[idx]:
		return

	cnt += 1
	temp[idx] = 1
	next_s = seniors[idx] - 1

	searching(next_s)

result = -1

for mem in range(len(seniors)):
	temp = [0] * n
	cnt = 0
	searching(mem)

	if result < cnt:
		result, member = cnt, mem
	
	
print(member+1)
