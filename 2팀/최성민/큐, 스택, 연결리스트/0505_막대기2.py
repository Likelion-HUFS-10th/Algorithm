x = int(input())

stack = [64]

def proceed(x):
	if x == 64:
		return 1

	while True:
		if sum(stack) > x:
			last = stack.pop()
			stack.append(last // 2)
		else:
			stack.append(stack[-1] // 2)
			
		if sum(stack) == x:
			break	

	return len(stack)

print(proceed(x))		
