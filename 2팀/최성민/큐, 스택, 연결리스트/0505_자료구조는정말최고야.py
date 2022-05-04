import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
answer = True

for i in range(m):
	cnt = int(input())
	book = list(map(int, input().split()))

	for idx in range(len(book)-1):
		if book[idx] < book[idx+1]:
			answer = False
			break
	
	if not answer:
		break

print("Yes" if answer else "No")
