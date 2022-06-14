a = int(input())

c2 = 0
arr = [-1] * (a+1)

def fib(n):
	global c2

	for i in range(1, n+1):
		if i == 1 or i == 2:
			arr[i] = 1
		else:
			arr[i] = arr[i-1] + arr[i-2]
			c2 += 1

	return arr[n]

print(fib(a), c2)
