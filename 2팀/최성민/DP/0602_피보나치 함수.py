t = int(input())

memo = [0] * 41

def fibo(n):
	one = 0
	zero = 0

	memo[0] = (1, 0)
	memo[1] = (0, 1)

	if n == 1:
		one += 1

	elif n == 0:
		zero += 1

	else:
		if memo[n] == 0:
			a1, a2 = fibo(n-1)
			b1, b2 = fibo(n-2)

			memo[n] = (a1 + b1, a2 + b2)

		return memo[n]

	return (zero, one)


for _ in range(t):
	n = int(input())
	print(*fibo(n))


