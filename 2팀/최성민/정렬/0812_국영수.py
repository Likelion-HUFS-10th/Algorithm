import sys
input = sys.stdin.readline

n = int(input())

_list = []

for _ in range(n):
	name, kor, eng, math = input().split()
	_list.append((int(kor), int(eng), int(math), name))

_list.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))

for item in _list:
	print(item[3])


