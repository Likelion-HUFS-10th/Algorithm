from re import A


n = int(input())
arr = [0] * (n+1)

def fib(n):
	for i in range(1, n+1):
		if i <= 2:
			arr[i] = 1
		
		else:
			arr[i] = arr[i-1] + arr[i-2]

	return f"{arr[-2]} {arr[-1]}"

print(fib(n))