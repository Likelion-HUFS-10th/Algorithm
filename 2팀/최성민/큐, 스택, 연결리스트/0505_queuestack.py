# Python3로 실행한 경우 시간복잡도와 공간복잡도 효율이 가장 높았음

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
types = list(map(int, input().split()))
items = list(map(int, input().split()))
m = int(input())
for_add = deque(map(int, input().split()))

queuestack = deque()
result = []

for i in range(n):
	if types[i] == 0:
		queuestack.append(items[i])

while for_add:
	temp = for_add.popleft()

	queuestack.appendleft(temp)
	result.append(queuestack.pop())

for i in range(len(result)):
	print(result[i], end=" ")
