n = int(input())

_list = []

for _ in range(n):
	a, b = input().split()
	
	_list.append((a, int(b)))

_list.sort(key=lambda x: x[-1])

for i in _list:
	print(i[0], end=" ")