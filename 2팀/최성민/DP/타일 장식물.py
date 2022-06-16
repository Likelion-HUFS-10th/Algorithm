n = int(input())
f = [0] * (n+2)

for i in range(1, n+2):
	if i == 1 or i == 2:
		f[i] = 1

	else:
		f[i] = f[i-1] + f[i-2]

print((f[-1] + f[-2]) * 2)