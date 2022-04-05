M = int(input())
N = int(input())

prime_list = []
nums = [True] * (N+1)

def prime(N):
	m = int(N ** 0.5)

	for i in range(2, m+1):
		if nums[i] == True:
			for j in range(i+i, N+1, i):
				nums[j] = False


prime(N)

for i in range(M, N+1):
	if i >= 2:
		if nums[i]:
			prime_list.append(i)

prime_list.sort()

if prime_list:
	print(sum(prime_list))
	print(prime_list[0])
else:
	print(-1)
