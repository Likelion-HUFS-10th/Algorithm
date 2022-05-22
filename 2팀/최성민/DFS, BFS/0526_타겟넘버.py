numbers = list(map(int, input().split()))
target = int(input())

numbers = [[i, -i] for i in numbers]
cnt = 0
value = []

def dfs(idx):
	global cnt

	if len(value) > len(numbers)-1:
		if sum(value) == target:
			cnt += 1
		return
	
	select = numbers[len(value)]
	
	for i in select:
		value.append(i)
		dfs(idx)
		value.pop()

dfs(0)
print(cnt)
