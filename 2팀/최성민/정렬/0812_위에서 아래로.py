n = int(input())

_list = []
for _ in range(n):
	_list.append(int(input()))

_list.sort(reverse=True)

print(*_list)

