# n = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
# result = [3, 4, 2, 1, 5]

# n = 4
# stages = [4, 4, 4, 4]

n = 5
stages = [1, 1, 1, 1, 1]

stay = [0] * (n + 1)

for i in range(len(stages)):
	stay[stages[i]-1] += 1

player = len(stages)
defeats = []
for idx in range(n):
	# print(f'{idx}번 스테이지 실패율: {stay[idx]} / {player}')
	if player:
		defeats.append((idx, stay[idx] / player))
	else:
		defeats.append((idx, 0))	
	player -= stay[idx]

answer = []
for item in sorted(defeats, key=lambda x: -x[1]):
	answer.append(item[0] + 1)

print(answer)

# ---------------------------------
"""
stay = [0] * (n + 1)

for i in range(len(stages)):
	stay[stages[i]-1] += 1

player = len(stages)
answer = []
for idx in range(n):
	# print(f'{idx}번 스테이지 실패율: {stay[idx]} / {player}')
	if player:
		answer.append((idx, stay[idx] / player))
	else:
		answer.append((idx, 0))	
	player -= stay[idx]

answer.sort(key=lambda x: -x[1])

answer = [i[0] + 1 for i in answer]

print(answer)
"""