import sys
input = sys.stdin.readline

T = int(input())
answer = []

def sorting(ea, arr):
	sales = []

	while ea != len(sales):
		temp = arr.pop(0)
		if temp // 0.75 in arr:
			sales.append(temp)
			arr.remove(temp // 0.75)
		print(arr)
	return sorted(sales)

for i in range(T):
	ea = int(input())
	items = list(map(int, input().split()))
	answer.append(sorting(ea, items))

for i in range(len(answer)):
	str_ = "Case #%d:"%(i+1)
	for j in answer[i]:
		str_ += ' %d'%j
	print(str_)
