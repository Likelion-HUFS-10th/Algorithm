import sys
from collections import deque
import copy
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	n, m = map(int, input().split())
	priority = deque(map(int, input().split()))
	p = copy.deepcopy(priority)

	priority = deque([priority[i], 'y'] if i == m else [priority[i], 'n'] for i in range(len(priority)))
	toggle = True
	cnt = 0

	while priority:
		max_p = max(p)
		p.remove(max_p)

		for item in list(priority):
			if item[0] == max_p: 
				cnt += 1
	
				if item[1] == "n":
					priority.remove(item)
					break
				
				elif item[1] == 'y':
					toggle = False
					break
			
			else:
				target = priority.popleft()
				priority.append(target)

		if not toggle:
			break

	print(cnt)

# deque mutated during iteration
# deque를 반복문 돌릴 때, deque의 내용이 변질되거나 크기가 변경될 때 발생하는 이유
# 해당 오류를 해결하기 위해 deque를 list로 바꿔서 사용하거나 copy 모듈을 사용한다.



